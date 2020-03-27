# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:58:07 2020

@author: Camilo
"""
import pandas as pd 
import numpy as np
from numpy.linalg import inv


def predictDatos(matrix_coef):
    
    #VALORES PARA TESTEAR (el primer valor 1 es por defecto, no se puede modificar!)
    x_test = [[1], [7.4], [0.7], [0.0], [1.9], [0.076], [11.0], [34.0], 
              [0.9978], [3.51], [0.56], [9.4]]
    
    for i in range(11):
        x_test[i+1][0]=(x_test[i+1][0]-min[i])/(max[i]-min[i])
    x_test=np.matrix(x_test)
    Y1=np.matmul( matrix_coef.T , x_test)   
    print(Y1*(max[-1]-min[-1])+min[-1])
    
    
    
data = pd.read_csv("winequality.csv")
#valores maximos de cada columna
max= [data[c].max() for c in data.columns] 
#valores minimos de cada columna
min= [data[c].min() for c in data.columns]

#mostrarDataSet(data)
#mostrarInfoDataSet(data)
   

i=0
for c in data.columns:
    while(i<len(data.columns)): 
        data[c]=(data[c]-min[i])/(max[i]-min[i])       
        i=i+1
        break
#print(data)

data_values = data.values
data_train_values=[]
out_train_values=[]
#dimensions of data set (1599,12)
dimension_data=data.shape

for i in range(dimension_data[0]):                      
    data_train_values.append((data_values[i][:-1]).tolist())
    out_train_values.append(data_values[i][-1])    
    
#print(data_train)

#matriz de unos
matrix_ones=np.ones((1591,1))
#b=np.matrix(x_train)

#matriz de datos de entrenamiento
xtrain_matrix=np.matrix(data_train_values)
xtrain_matrix=np.concatenate((matrix_ones,xtrain_matrix),axis=1)
xtrain_matrixT=xtrain_matrix.T #Transpuesta
 
#matrix de datos de salida
out_train_matrix = np.matrix(out_train_values)
out_train_matrix = out_train_matrix.T #Transpuesta
print(out_train_matrix)
#Matrix inversa
matrix_inversa=np.linalg.inv(np.matmul( xtrain_matrixT , xtrain_matrix ))

f=np.matmul( matrix_inversa , xtrain_matrixT )
matrix_coeficientes=np.matmul( f , out_train_matrix)    

predictDatos(matrix_coeficientes)

    
