import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

# from sklearn.preprocessing import StandardScaler

train_fn = 'timelines'
# test_fn = 'college'
num_cols = 0

def read_csv(fn):  # read csv and scale data
    raw = pd.read_csv(fn + '.csv')
    # print(raw['date'])
    raw = raw.dropna()
    return raw.copy()

df = read_csv(train_fn)
df['date'] = df['date'].astype('datetime64[ns]')
print(df)
cols = df.columns
num_cols = len(cols)

def features(df):
    y_tmp = df[['followers']]
    x_tmp = df.iloc[:,1:3]
    print(x_tmp.shape)

    X = torch.FloatTensor(x_tmp.values)
    Y = torch.FloatTensor(y_tmp.values)
    print(X)
    return X, Y

X, Y = features(df)    

class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)  # its num_cols = 1 because the 1 is the label

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred

net = Net()

loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss
optimizer = torch.optim.SGD(net.parameters(), lr=0.001)

def run(data, labels):  # train == 1, test == else
    for epoch in range(500):
        y_pred = net(data)
        print('predicted: ' + str(y_pred[epoch].item()))
        print('real: ' + str(labels[epoch].item()))
        error = y_pred - labels
        print('error: ' + str(error[epoch].item()))
        loss = loss_func(y_pred, labels) 
        print(loss)
        plt.scatter(epoch, loss.item(), color='r', s=10, marker='o')

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

run(X, Y)

plt.show()