#-----------------------------------------------
#Taller resolver sistemas de ecuaciones lineales
#Esteban Moreno Castillo
#-----------------------------------------------
import numpy as np

A = np.array([[1,10,100], [1,12,144], [1,14,196]])
b = np.array([12,18,21])
x = np.linalg.solve(A, b)
print(x)
