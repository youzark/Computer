import torch
import numpy as np
from torch import nn, autograd
from torch.utils.data import DataLoader, Dataset
from models.Nets import CNNMnist
import copy
from phe import paillier

class DatasetSplit(Dataset):
    def __init__(self, dataset, idxs):
        self.dataset = dataset
        self.idxs = list(idxs)

    def __len__(self):
        return len(self.idxs)

    def __getitem__(self, item):
        image, label = self.dataset[self.idxs[item]]
        return image, label

pub,priv = paillier.generate_paillier_keypair()
class Client():
    def __init__(self, args, dataset=None, idxs=None, w = None,C = 0.5,sigma = 0.05):
        self.args = args
        self.loss_func = nn.CrossEntropyLoss()
        self.ldr_train = DataLoader(DatasetSplit(dataset, idxs), batch_size=self.args.local_bs, shuffle=True)
        self.model = CNNMnist(args=args).to(args.device)
        self.model.load_state_dict(w)
        self.C = C
        self.sigma = sigma
        if self.args.mode == 'Paillier':
            self.pub = pub
            self.priv = priv
        
    def train(self):
        w_old = copy.deepcopy(self.model.state_dict())
        net = copy.deepcopy(self.model)

        net.train()
        
        #train and update
        optimizer = torch.optim.SGD(net.parameters(), lr=self.args.lr, momentum=self.args.momentum)
        for iter in range(self.args.local_ep):
            batch_loss = []
            for batch_idx, (images, labels) in enumerate(self.ldr_train):
                images, labels = images.to(self.args.device), labels.to(self.args.device)
                net.zero_grad()
                log_probs = net(images)
                loss = self.loss_func(log_probs, labels)
                loss.backward()
                optimizer.step()
                batch_loss.append(loss.item())
        
        w_new = net.state_dict()

        update_w = {}
        if self.args.mode == 'plain':
            for k in w_new.keys():
                update_w[k] = w_new[k] - w_old[k]
        # 1. part one
        #     DP mechanism
        elif self.args.mode == 'DP':
            for k in w_new.keys():
                # calculate update_w
                update_w[k] = w_new[k] - w_old[k]
                # clip the update
                update_w[k] = update_w[k] / max(1,torch.norm(update_w[k],2)/self.C)
                # add noise ,cause update_w might reveal user's data also ,we should add noise before send to server
                update_w[k] += np.random.normal(0.0,self.sigma**2 * self.C**2)
        # 2. part two
        #     Paillier enc
        elif self.args.mode == 'Paillier':
            print(len(w_new.keys()))
            for k in w_new.keys():
                print("start  ",k,flush=True)
                update_w[k] = w_new[k] - w_old[k]
                update_w_list = update_w[k].view(-1).cpu().tolist()
                for iter,w in enumerate(update_w_list):
                    update_w_list[iter] = self.pub.encrypt(w)
                update_w[k] = update_w_list
                print("end ",flush=True)
        else:
            exit()
        return update_w, sum(batch_loss) / len(batch_loss)

    def update(self, w_glob):
        if self.args.mode == 'plain':
            self.model.load_state_dict(w_glob)
        elif self.args.mode == 'DP':
            self.model.load_state_dict(w_glob)
        elif self.args.mode == 'Paillier':
            w_glob_ciph = copy.deepcopy(w_glob)
            for k in w_glob_ciph.keys():
                for iter,item in enumerate(w_glob_ciph[k]):
                    w_glob_ciph[k][iter] = self.priv.decrypt(item)
                shape =list(self.model.state_dict()[k].size())
                w_glob_ciph[k] = torch.FloatTensor(w_glob_ciph[k]).to(self.args.device).view(*shape)
                self.model.state_dict()[k] += w_glob_ciph[k]
        else:
            exit()
