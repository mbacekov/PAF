import gravity as grav
import matplotlib.pyplot as plt
import numpy as np

Zemlja = grav.Planet(5.9742 * 10**24, np.array((float(-1.496 * 10**11), 0.)), np.array((0., float(29783))), np.array((0., 0.)))
Sunce = grav.Planet(1.989 * 10**30, np.array((0., 0.)), np.array((0., 0.)), np.array((0., 0.)))

svemir = grav.Universe()
svemir.add_planet(Zemlja)
svemir.add_planet(Sunce)

svemir.trajectory(365.242*24*60*60, 3600)

plt.plot(Zemlja.x, Zemlja.y)
plt.scatter(Sunce.x, Sunce.y, color='blue')
plt.axis('equal')
plt.grid()
plt.show()