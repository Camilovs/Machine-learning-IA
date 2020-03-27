# Imports necesarios
import csv
import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

def mostrarDataSet(data):
    print(data)
    
def mostrarInfoDataSet(data):
    print(data.describe())

def printListaFull(lista):
    for x in lista:
        print (x)
def crearFileCsv():
        file = open("predict.csv", "w", newline='')
        spamreader = csv.writer(file)
        spamreader.writerow(out_pred)
        file.close()
        
#cargamos los datos de entrada
data = pd.read_csv("winequality.csv")
#datos sin la salida esperada, seria el conjunto de entrenamiento
data2  = pd.read_csv("winequality.csv")
del data2['quality']

mostrarDataSet(data)
mostrarInfoDataSet(data)


#Conjunto de entrenamiento
multiData_train = np.array(data2)
#Salidas del conjunto
out_train = data['quality'].values


# Creamos un nuevo objeto de Regresión Lineal
regr = linear_model.LinearRegression()

#Entrenamos
regr.fit(multiData_train, out_train)
 
# Hacemos la predicción con los mismos datos sin la salida 
out_pred = regr.predict(multiData_train)
 
# Los coeficientes
print('Coeficientes: \n', regr.coef_)
# Salidas predichas
print('Valores de prediccion: ', out_pred)

#printListaFull(out_pred)
#crearFileCsv()

# Error cuadrático medio
print("Error cuadratico medio: %.2f" % mean_squared_error(out_train, out_pred))
# Evaluamos el puntaje de varianza (siendo 1.0 el mejor posible)
print('Variancia: %.2f' % r2_score(out_train, out_pred))