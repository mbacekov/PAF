import universe as un
import matplotlib.pyplot as plt
import numpy as np

Au = 1.496e11

Zemlja = un.Planet(5.9742 * 10**24, np.array((float(-1.496 * 10**11), 0.)), np.array((0., float(29783))), 6.371*1e6)
Sunce = un.Planet(1.989 * 10**30, np.array((0., 0.)), np.array((0., 0.)), 0.696*1e9)
Merkur = un.Planet(3.3 * 10**24, np.array((0., 0.466 * 1.496 * 10**11)), np.array((-47362., 0.)), 2.439*1e6)
Venera = un.Planet(4.8685*10**24, np.array((0.723*1.496*10**11, 0.)), np.array((0., 35020.)), 6.051*1e6)
Mars = un.Planet(6.417*10**23, np.array((0., -1.666*1.496*10**11)), np.array((24007., 0.)), 3.389*1e6)

Komet = un.Planet(10**14, np.array((4.*Au, 4*Au)), np.array((-20000., -15000.)), 0.5*1e3)

svemir = un.Universe()
svemir.add_planet(Zemlja)
svemir.add_planet(Sunce)
svemir.add_planet(Merkur)
svemir.add_planet(Venera)
svemir.add_planet(Mars)
svemir.add_planet(Komet)

svemir.trajectory(5*365.242*24*60*60, 3600*24)

plt.plot(Zemlja.x, Zemlja.y, color='blue', label='Zemlja')
plt.plot(Zemlja.x[-1], Zemlja.y[-1], 'o', color='blue')

plt.plot(Merkur.x, Merkur.y, color='orange', label='Merkur')
plt.plot(Merkur.x[-1], Merkur.y[-1], 'o', color='orange')

plt.plot(Mars.x, Mars.y, color='grey', label='Mars')
plt.plot(Mars.x[-1], Mars.y[-1], 'o', color='grey')

plt.plot(Venera.x, Venera.y, color='red', label='Venera')
plt.plot(Venera.x[-1], Venera.y[-1], 'o', color='red')

plt.plot(Komet.x, Komet.y, color='pink', label='Komet')
plt.plot(Komet.x[-1], Komet.y[-1], 'o', color='pink')

plt.scatter(Sunce.x, Sunce.y, color='yellow', label='Sunce')

plt.legend(loc='upper right')
plt.grid()
plt.xlim(-2*Au, 2*Au)
plt.ylim(-2*Au, 2*Au)
plt.show()




