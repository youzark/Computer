import numpy as np
import math
from collections import Counter
from process_data import load_and_process_data
from evaluation import get_micro_F1,get_macro_F1,get_acc

class norm_pdf:
    def __init__(self,mean,standard_derivation):
        self.mean = mean
        self.standard_derivation = standard_derivation

    def log_pdf(self,value):
        part1 = 1 / (self.standard_derivation * math.pi)
        part2 = (value - self.mean)*(value - self.mean)/self.standard_derivation/self.standard_derivation/2
        part3 = math.exp(-part2)
        return math.log(part1 * part3)

class NaiveBayes:
    '''参数初始化
    Pc: P(c) 每个类别c的概率分布
    Pxc: P(c|x) 每个特征的条件概率
    '''
    def __init__(self):
        self.Pc={}
        self.Pxc={}

    '''
    通过训练集计算先验概率分布p(c)和条件概率分布p(x|c)
    建议全部取log，避免相乘为0
    '''
    #adopt gaussian method
    def fit(self,traindata,trainlabel,featuretype):
        # prior probobility
        data_size = traindata.shape[0]
        n = 3 # there possible gender record
        lable_count = [0,0,0]
        for iter in range(trainlabel.shape[0]):
            if trainlabel[iter][0] == 1:
                lable_count[0] += 1
            elif trainlabel[iter][0] == 2:
                lable_count[1] += 1 
            else:
                lable_count[2] += 1
        self.Pc[1] = (lable_count[0] + 1) / (data_size + n)
        self.Pc[2] = (lable_count[1] + 1) / (data_size + n)
        self.Pc[3] = (lable_count[2] + 1) / (data_size + n)

        # posterior probobility
        # discrete feature: gender
        fea_count = {}
        for iter in range(trainlabel.shape[0]):
            if (trainlabel[iter][0],traindata[iter][0]) in fea_count:
                fea_count[(trainlabel[iter][0],traindata[iter][0])] += 1
            else:
                fea_count[(trainlabel[iter][0],traindata[iter][0])] = 1
        for fea_key in fea_count:
            self.Pxc[fea_key] = math.log(fea_count[fea_key] + 1) - math.log(lable_count[fea_key[0] - 1] + 3)
        
        # continuous feature
        # all possible label
        for label in range(1,4):
            label_data = traindata
            #select data with specific lable
            for iter in range(trainlabel.shape[0]):
                if trainlabel[iter][0] != label:
                    np.delete(label_data,iter,0)
            # calculate mean and derivation for specific (label,feature)
            for feature in range(1,8):
            #calculate mean and dev for each possible lable
                mean = np.mean(label_data[:,feature])
                std_dev = np.std(label_data[:,feature])
            #get normal pdf and append it to self.pxc
                norm = norm_pdf(mean,std_dev)
                self.Pxc[(1,label,feature)] = norm

        print(self.Pxc)
        
        
        '''
        需要你实现的部分
        '''
    '''
    根据先验概率分布p(c)和条件概率分布p(x|c)对新样本进行预测
    返回预测结果,预测结果的数据类型应为np数组，shape=(test_num,1) test_num为测试数据的数目
    feature_type为0-1数组，表示特征的数据类型，0表示离散型，1表示连续型
    '''
    def predict(self,features,featuretype):
        for iter in features.shape[0]:
            prob = []
            for type_id in range(1,4):
                prob[type_id] = self.Pc[type_id] 
                # feature gender
                prob[type_id] *= self.Pxc[(type_id,features[iter][0])]
                # other continuous features
                for feature_id in range(1,8):
                    prob[type_id] *= self.Pxc[feature_id]


        
        '''
        需要你实现的部分
        '''       


def main():
    # 加载训练集和测试集
    train_data,train_label,test_data,test_label=load_and_process_data()
    feature_type=[0,1,1,1,1,1,1,1] #表示特征的数据类型，0表示离散型，1表示连续型
    Nayes=NaiveBayes()
    Nayes.fit(train_data,train_label,feature_type) # 在训练集上计算先验概率和条件概率
    print(Nayes.Pc)
    pred=Nayes.predict(test_data,feature_type)  # 得到测试集上的预测结果

    # 计算准确率Acc及多分类的F1-score
    print("Acc: "+str(get_acc(test_label,pred)))
    print("macro-F1: "+str(get_macro_F1(test_label,pred)))
    print("micro-F1: "+str(get_micro_F1(test_label,pred)))

main()
