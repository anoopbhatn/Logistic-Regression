# To Generate Dataset in matrix form

import numpy as np 
import csv

f=open("iris.data","r")

reader=csv.reader(f,delimiter=',')
data=[]
for row in reader:
	data.append(row)
	
data_list=data
data=np.matrix(data)