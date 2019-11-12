-----------------------------------------------
Taller problema interpolación temperatura 
Esteban Moreno Castillo
-----------------------------------------------
from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt 

hora=[6,8,10,12,14,16,18,20]
grados=[7,9,12,18,21,19,15,10]

p=lagrange(hora,grados)
x1=np.linspace(min(grados),max(grados),10)
y1=p(x1)

plt.plot(x1,y1,label='interpolación')
plt.plot(hora,grados,'x', mew=2, label='Datos importados')

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
print(p(17))

# Gráfico de la predicción de temperatura a las 17 horas
plt.plot(17, p(17), 'r.')

plt.show()
