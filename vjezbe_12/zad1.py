import universe as un
import matplotlib.pyplot as plt
import numpy as np

Zemlja = un.Planet(5.9742 * 10**24, np.array((float(-1.496 * 10**11), 0.)), np.array((0., float(29783))))
Sunce = un.Planet(1.989 * 10**30, np.array((0., 0.)), np.array((0., 0.)))
Merkur = un.Planet(3.3 * 10**24, np.array((0., 0.466 * 1.496 * 10**11)), np.array((-47362., 0.)))
Venera = un.Planet(4.8685*10**24, np.array((0.723*1.496*10**11, 0.)), np.array((0., 35020.)))
Mars = un.Planet(6.417*10**23, np.array((0., -1.666*1.496*10**11)), np.array((24007., 0.)))

svemir = un.Universe()
svemir.add_planet(Zemlja)
svemir.add_planet(Sunce)
svemir.add_planet(Merkur)
svemir.add_planet(Venera)
svemir.add_planet(Mars)

svemir.trajectory(5*365.242*24*60*60, 3600*24)

plt.plot(Zemlja.x, Zemlja.y, color='blue', label='Zemlja')
plt.plot(Zemlja.x[-1], Zemlja.y[-1], 'o', color='blue')

plt.plot(Merkur.x, Merkur.y, color='orange', label='Merkur')
plt.plot(Merkur.x[-1], Merkur.y[-1], 'o', color='orange')

plt.plot(Mars.x, Mars.y, color='grey', label='Mars')
plt.plot(Mars.x[-1], Mars.y[-1], 'o', color='grey')

plt.plot(Venera.x, Venera.y, color='red', label='Venera')
plt.plot(Venera.x[-1], Venera.y[-1], 'o', color='red')

plt.scatter(Sunce.x, Sunce.y, color='yellow', label='Sunce')
plt.axis('equal')
plt.legend(loc='upper right')
plt.grid()
plt.show()




