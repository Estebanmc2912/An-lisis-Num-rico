#-----------------------------------------------
#Taller solución de bezier con libreria matplotlib
#Esteban Moreno Castillo
#-----------------------------------------------


import matplotlib.path as mpath
import matplotlib.patches as mpatches

import matplotlib.pyplot as plt

Path = mpath.Path
fig, ax = plt.subplots()
puntos = mpatches.PathPatch(
    Path([(1, 1), (1, 3), (3, 3), (2, 2)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]),
    fc="none", transform=ax.transData)

ax.add_patch(puntos)
plt.show()
