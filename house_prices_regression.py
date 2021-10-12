# -*- coding: utf-8 -*-
"""house_prices_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QNk5OBWqRQHdsi-kCfZjJIldVIRI1Apx
"""

import pandas as pd 
import numpy as np
import math
import csv

"""#**Importing the dataset**"""

data = pd.read_csv("train.csv")
x_df = data.loc[:,["MSSubClass","LotArea","OverallQual","OverallCond","YearBuilt","1stFlrSF","2ndFlrSF","GrLivArea","GarageArea","YrSold"]]
x = x_df.values 
y = data.iloc[:,-1].values

"""##**features scalling**"""

scal_fact = x_df.max().values
x = x/scal_fact
x_train = x  
y_train = y
y_train=np.ones((len(y),1))
y_train = y.reshape(len(y),1)

"""#**training the model**

##**A) training the linear regression model**
"""

x_train1 = np.c_[np.ones(len(x_train)),x_train]
count = 0
i = []
theta1 = np.random.rand(len(x_train1[0]),1)
lr = 0.1
loss = []
saving_cnt=0

with open("theta_linear_reg", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     while (True):
      y_pred = np.matmul(x_train1,theta1)
      grad = np.matmul(np.transpose(x_train1) , np.subtract(y_pred,y_train))/len(x_train)
      theta1 = np.subtract(theta1,lr*grad)
      loss.append(np.sum(np.square(np.subtract(y_pred,y_train)))/(len(x_train1)))
      i.append(count)
      count+=1
      print(f"at iteration{count} loss = {loss[-1]}")
      saving_cnt +=1
      if(saving_cnt%1000==0):
        wr.writerow(theta1)

"""##**B) training the 2nd-degree non-linear model**"""

x_train2 = np.c_[np.ones(len(x_train)),x_train,np.square(x_train)]
prev_loss = -math.inf 
current_loss = math.inf
count = 0
i = []
theta2 = np.random.rand(len(x_train2[0]),1)
lr = 0.1
loss = []
saving_cnt=0


with open("theta_2nd-degree_reg", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     while (True):
      y_pred = np.matmul(x_train2,theta2)
      grad = np.matmul(np.transpose(x_train2) , np.subtract(y_pred,y_train))/len(x_train2)
      theta2 = np.subtract(theta2,lr*grad)
      loss.append(np.sum(np.square(np.subtract(y_pred,y_train)))/(len(x_train2)))
      i.append(count)
      print(f"at iteration {count} loss = {loss[-1]}")
      count+=1
      saving_cnt +=1
      if(saving_cnt%1000==0):
        wr.writerow(theta2)

"""##**C) training the 3rd-degree non-linear model**

"""

x_train3 = np.c_[np.ones(len(x_train)),x_train,np.square(x_train),np.power(x_train,3)]
prev_loss = -math.inf 
current_loss = math.inf
count = 0
i = []
theta3 = np.random.rand(len(x_train3[0]),1)
lr = 0.1
loss = []
saving_cnt=0

with open("theta_3rd-degree_reg", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     while (True):
      y_pred = np.matmul(x_train3,theta3)
      grad = np.matmul(np.transpose(x_train3) , np.subtract(y_pred,y_train))/len(x_train3)
      theta3 = np.subtract(theta3,lr*grad)
      loss.append(np.sum(np.square(np.subtract(y_pred,y_train)))/(len(x_train3)))
      i.append(count)
      count+=1
      print(f"at iteration {count} loss = {loss[-1]}")
      saving_cnt +=1
      if(saving_cnt%1000==0):
        wr.writerow(theta3)


print(loss)

"""#**Testing and Evaluating the model**

##**A) Read the test set**
"""

test_data = pd.read_csv("test.csv")
x_df = test_data.loc[:,["MSSubClass","LotArea","OverallQual","OverallCond","YearBuilt","1stFlrSF","2ndFlrSF","GrLivArea","GarageArea","YrSold"]]
x = x_df.fillna(0).values
y = test_data.iloc[:,-1].values

"""##**B) Reading the thetas for the three models**"""

data1 = pd.read_csv("theta_linear_reg.csv")
theta1 = data1.iloc[-1,:].values

data2 = pd.read_csv("theta_2nd-degree_reg.csv")
theta2 = data2.iloc[-1,:].values

data3 = pd.read_csv("theta_3rd-degree_reg.csv")
theta3 = data3.iloc[-1,:].values

"""##**C) Scalling the testset features**"""

scal_fact = x_df.max().values
x = x/scal_fact
x_test = x  
y_test = y

x_test1 = np.c_[np.ones(len(x_test)),x_test]
x_test2 = np.c_[np.ones(len(x_test)),x_test,np.square(x_test)]
x_test3 = np.c_[np.ones(len(x_test)),x_test,np.square(x_test),np.power(x_test,3)]

"""##**D) Predicting the results**"""

y_pred1 = np.matmul(x_test1,theta1)
y_pred2 = np.matmul(x_test2,theta2)
y_pred3 = np.matmul(x_test3,theta3)

print("============================[Linear-regression]=============================")
print(y_pred1)
print("\n\n======================[2nd-order-nonlinear-regression]======================")
print(y_pred2)
print("\n\n======================[3rd-order-nonlinear-regression]======================")
print(y_pred3)

"""##**E) Calculate the loss for each model**"""

y_test=y_test.reshape(len(y_test),1)
y_pred1=y_pred1.reshape(len(y_pred1),1)
y_pred2=y_pred2.reshape(len(y_pred2),1)
y_pred3=y_pred3.reshape(len(y_pred3),1)

test1_loss = np.sum(np.square(np.subtract(y_pred1,y_test)))
test2_loss = np.sum(np.square(np.subtract(y_pred2,y_test)))
test3_loss = np.sum(np.square(np.subtract(y_pred3,y_test)))

"""##**F) Selecting the best model for the dataset**"""

print(f"linear regression model:                  loss = {test1_loss}")
print(f"2nd-degree non-linear regression model:   loss = {test2_loss}")
print(f"3rd-degree non-linear regression model:   loss = {test3_loss}")
print("---------------------------------------------------------------------")
if(test1_loss<test2_loss):
  if (test1_loss<test3_loss):
    best_model = "linear regression model"
    best_loss = test1_loss
  elif (test2_loss<test3_loss):
    best_model = "2nd-degree non-linear regression model"
    best_loss = test2_loss
  else: 
    best_model = "3rd-degree non-linear regression model"
    best_loss = test3_loss

print(f"\nthe best model is :                       {best_model}")
print(f"the best loss is :                        {best_loss}")