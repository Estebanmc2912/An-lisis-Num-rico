
#-----------------------------------------------
#Taller solución Curvas
#Esteban Moreno Castillo
#-----------------------------------------------


import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

Path = mpath.Path
fig, ax = plt.subplots()
puntos = mpatches.PathPatch(
    Path([(0, 2), (1, 2), (2, 3), (1, 0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]),
    fc="none", transform=ax.transData)
    
ax.add_patch(pp1)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Test gráfica curvas')
fig1, ax1 = plt.subplots()

puntos = mpatches.PathPatch(
    Path([(1, 0), (0.25, -0.5), (0.75, -0.5), (0.5, 0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]),
    fc="none", transform=ax1.transData)

ax.add_patch(puntos)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Test gráfica curvas')
plt.show()
