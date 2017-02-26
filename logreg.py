# Logistic Regression on Iris Dataset

import numpy as np 
from sklearn.linear_model import LogisticRegression
from dataset import data,data_list

# Extract only attribute information from data
x=data[:,:4]
x=np.array(x)

# List to store converted float values for the attributes
x1=[]
# Getting values in float
for i in range(len(x)):
	x1.append([])
	for j in range(len(x[0])):
		x1[i].append(float(x[i][j]))

# Matrix of values of all 4 attributes
x=np.matrix(x1)

y=[]
# Matrix of all the class labels for all records
for i in data_list:
	y.append(i[-1])
#y=np.matrix(y)

# An instance of LogisticRegression
logistic = LogisticRegression()
# Fit the data
logistic.fit(x,y)

print 'Enter a comma separated line of input for sepal length,sepal width,petal length,petal width'
query=map(float,raw_input().split(','))
query=np.matrix(query)

# Predict the class label
res=logistic.predict(query)

print '\n','The predicted class for the given attributes - ',res[0]