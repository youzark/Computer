import numpy as np
import cvxopt #用于求解线性规划
from process_data import load_and_process_data
from evaluation import get_micro_F1,get_macro_F1,get_acc


#根据指定类别main_class生成1/-1标签
def svm_label(labels,main_class):
    new_label=[]
    for i in range(len(labels)):
        if labels[i]==main_class:
            new_label.append(1)
        else:
            new_label.append(-1)
    return np.array(new_label)

# 实现线性回归
class SupportVectorMachine:

    '''参数初始化 
    lr: 梯度更新的学习率
    Lambda: L2范数的系数
    epochs: 更新迭代的次数
    '''
    def __init__(self,kernel,C,Epsilon):
        self.kernel=kernel
        self.C = C
        self.Epsilon=Epsilon

    '''KERNEL用于计算两个样本x1,x2的核函数'''
    def KERNEL(self, x1, x2, kernel='Gauss', d=2, sigma=1):
        #d是多项式核的次数,sigma为Gauss核的参数
        K = 0
        if kernel == 'Gauss':
            K = np.exp(-(np.sum((x1 - x2) ** 2)) / (2 * sigma ** 2))
        elif kernel == 'Linear':
            K = np.dot(x1,x2)
        elif kernel == 'Poly':
            K = np.dot(x1,x2) ** d
        else:
            print('No support for this kernel')
        return K

    '''
    根据训练数据train_data,train_label（均为np数组）求解svm,并对test_data进行预测,返回预测分数，即svm使用符号函数sign之前的值
    train_data的shape=(train_num,train_dim),train_label的shape=(train_num,) train_num为训练数据的数目，train_dim为样本维度
    预测结果的数据类型应为np数组，shape=(test_num,1) test_num为测试数据的数目
    '''
    def fit(self,train_data,train_label,test_data):

        data_size = train_data.shape[0]
        K = np.zeros((data_size,data_size))
        for i in range(data_size):
            for j in range(data_size):
                K[i,j] = self.KERNEL(train_data[i], train_data[j])
        y_mat1 = np.tile(train_label,(data_size,1))
        y_mat2 = np.transpose(y_mat1)
        train_label = np.array(train_label).reshape(len(train_label),1)
        h_mat = K * y_mat1 * y_mat2
        p_mat = cvxopt.matrix(h_mat)
        q_mat = cvxopt.matrix(-np.ones((data_size,1)))
        g_mat = cvxopt.matrix(np.vstack((-np.eye(data_size),np.eye(data_size))))
        h_vec = cvxopt.matrix(np.hstack((np.zeros(data_size),self.C*np.ones(data_size))))
        a_mat = cvxopt.matrix(train_label.astype(float).reshape(1,-1))
        b_sca = cvxopt.matrix(np.zeros(1))

        cvxopt.solvers.options['abstol'] = self.Epsilon
        cvxopt.solvers.options['reltol'] = self.Epsilon 
        cvxopt.solvers.options['feastol'] = self.Epsilon 
        sol = cvxopt.solvers.qp(p_mat,q_mat,g_mat,h_vec,a_mat,b_sca)
        alphas = np.array(sol['x'])


        ind = (alphas > self.Epsilon).flatten()
        y_sat = train_label[ind]
        x_sat = train_data[ind]
        alpha_sat = alphas[ind]
        b = y_sat[0][0]
        for iter in range(y_sat.shape[0]):
            b -= alpha_sat[iter]*y_sat[iter]*self.KERNEL(x_sat[0],x_sat[iter])
        
        
        test_size = test_data.shape[0]
        pred = np.zeros((test_size,1))
        for iter in range(test_size):
            pred[iter] = b
            for id in range(y_sat.shape[0]):
                pred[iter] += alpha_sat[id]*y_sat[id]*self.KERNEL(train_data[id],test_data[iter])

        return pred

        '''
        需要你实现的部分
        '''





def main():
    # 加载训练集和测试集
    Train_data,Train_label,Test_data,Test_label=load_and_process_data()
    Train_label=[label[0] for label in Train_label]
    Test_label=[label[0] for label in Test_label]
    train_data=np.array(Train_data)
    test_data=np.array(Test_data)
    test_label=np.array(Test_label).reshape(-1,1)
    #类别个数
    num_class=len(set(Train_label))


    #kernel为核函数类型，可能的类型有'Linear'/'Poly'/'Gauss'
    #C为软间隔参数；
    #Epsilon为拉格朗日乘子阈值，低于此阈值时将该乘子设置为0
    kernel='Linear' 
    C = 1
    Epsilon=10e-5
    #生成SVM分类器
    SVM=SupportVectorMachine(kernel,C,Epsilon)

    predictions = []
    #one-vs-all方法训练num_class个二分类器
    for k in range(1,num_class+1):
        #将第k类样本label置为1，其余类别置为-1
        train_label=svm_label(Train_label,k)
        # 训练模型，并得到测试集上的预测结果
        prediction=SVM.fit(train_data,train_label,test_data)
        predictions.append(prediction)
    predictions=np.array(predictions)
    #one-vs-all, 最终分类结果选择最大score对应的类别
    pred=np.argmax(predictions,axis=0)+1

    # 计算准确率Acc及多分类的F1-score
    print("Acc: "+str(get_acc(test_label,pred)))
    print("macro-F1: "+str(get_macro_F1(test_label,pred)))
    print("micro-F1: "+str(get_micro_F1(test_label,pred)))

main()
