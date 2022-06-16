import universe as un
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import PillowWriter
import math

Au = 1.486*10**11

Zemlja = un.Planet(5.9742 * 10**24, np.array((float(-1.496 * 10**11), 0.)), np.array((0., float(-29783))))
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

fig = plt.figure()
metadata = dict(title='Suncev_sustav', artist='Marija')
writer = PillowWriter(fps=15, metadata=metadata)


with writer.saving(fig, "animacija.gif", 100):
    for j in range(math.floor(len(Zemlja.x)/10)):
        i = j*10
        plt.clf()

        plt.plot(Zemlja.x[0:i], Zemlja.y[0:i], color="blue", label="Zemlja")
        plt.plot(Zemlja.x[i], Zemlja.y[i], 'o', color="blue")

        plt.plot(Merkur.x[0:i], Merkur.y[0:i], color="orange", label="Merkur")
        plt.plot(Merkur.x[i], Merkur.y[i], 'o', color="orange")

        plt.plot(Mars.x[0:i], Mars.y[0:i], color="grey", label="Mars")
        plt.plot(Mars.x[i], Mars.y[i], 'o', color="grey")

        plt.plot(Venera.x[0:i], Venera.y[0:i], color="red", label="Venera")
        plt.plot(Venera.x[i], Venera.y[i], 'o', color="red")

        plt.scatter(Sunce.x[i], Sunce.y[i], color='yellow', label="Sunce")


        plt.legend(loc='upper right')
        plt.xlim(-2*Au, 2*Au)
        plt.ylim(-2*Au, 2*Au)
        plt.grid()
        plt.title('Sunčev sustav')

        writer.grab_frame()



