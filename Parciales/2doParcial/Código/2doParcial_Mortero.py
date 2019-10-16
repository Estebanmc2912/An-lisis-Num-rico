#!/usr/bin/env python
#-* coding: utf-8
 
#Librerías
from scipy import interpolate
import numpy as np
import visvis
from scipy.interpolate import interp1d, splrep, splev
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
 
x=[0,0, 3, 0, -3    ,9,7,10,9,4,6,     0,-7,-10,-9,-4,-6,  -9,-7,-10,-9,-4,-6,  6 ,10,9,4,7  ]
y=[0 ,3, 0, -3, 0    ,0,4,9,10,7,6,      9,4,9,10 ,7,6,      0,-4,-9,-10,-7,-6,   -6,-9,-10,-7,-4    ]
z=[0, 0, 0, 0,  0    ,9,8, 9,9,8,5,   9,8,9,9,8,5,        9,8,9,9,8,5,              5,9,9,8,8  ]    


# construcción de la grilla
spline = interpolate.Rbf(x,y,z,function='thin-plate')
#spline1 = interpolate.Rbf(x,y,z,function='thin-plate')
#spline1 = interpolate.Rbf(x,y,z,function='inverse')
#spline1 = interpolate.Rbf(x,y,z,function='multiquadric')
#spline1 = interpolate.Rbf(x,y,z,function='cubic')
#spline1 = interpolate.Rbf(x,y,z,function='gaussian')
spline1 = interpolate.Rbf(x,y,z,function='linear')

xi = np.linspace(min(x), max(x))
yi = np.linspace(min(y), max(y))
X, Y = np.meshgrid(xi, yi)

#'multiquadric': sqrt((r/self.epsilon)**2 + 1)
#'inverse': 1.0/sqrt((r/self.epsilon)**2 + 1)


#x2 = np.linspace(min(x2), max(x2))
#y2 = np.linspace(min(y2), max(y2))
#X2, Y2 = np.meshgrid(x2, y2)
 
# interpolación
Z  = spline(X,Y)
Z1 = spline1(X,Y)
#Visualización con visvis
f = visvis.gca()
m = visvis.plot(x,y,z, lc='k', ls='', mc='g', mw=10, lw=10, ms='.')
f.daspect = 1,1,10 # z x 10
#m = visvis.surf(xi,yi,Z)
m = visvis.surf(xi,yi,Z)
m = visvis.grid(xi,yi,Z1)


m.colormap = visvis.CM_JET 
f.axis.visible = True

#m = visvis.surf(x2,y2,Z2)
#m.colormap = visvis.CM_JET 


#Volumen en cada interpolación con respecto a los puntos:
#volume = Convexhull(xyz).volume

# Necesario para que la vista no se cierre
app = visvis.use()

#Movimiento cámara en 3 dimensiones (FPS)
a = visvis.gca()
a.camera='fly'
print(a.camera)


a = np.random.normal(size=(1000,3))
pp = Pointset(a)
pp *= Point(2,5,1)
l = visvis.plot(pp, ms='.', mc='r', mw='9', ls='', mew=0 )
l.alpha = 0.1

app.Run()

