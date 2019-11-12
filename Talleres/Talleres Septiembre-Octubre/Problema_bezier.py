#-----------------------------------------------
#Taller solución con Bezier
#Esteban Moreno Castillo
#-----------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import bezier

nodos = np.asfortranarray([[1.0, 1.0, 3.0, ],[1.0, 3.0, 3.0, ],])
curve1 = bezier.Curve.from_nodes(nodos, degree=2)
ax = curve1.plot(num_pts=256)
plt.show()
