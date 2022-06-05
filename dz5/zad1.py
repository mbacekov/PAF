import particle as prt
import numpy as np
import matplotlib.pyplot as plt

# q, m, B, E, v

def B_const(t):
	return np.array([0., 0., 1.])

def B_prom(t):
	return np.array([0., 0., 0.1*t[-1]])

prt1 = prt.Particle(-1, 1, B_const, np.array((0, 0, 0)), np.array((1., 1., 1.)))
prt1.RK4_trajectory(0.01)

prt2 = prt.Particle(-1, 1, B_prom, np.array((0, 0, 0)), np.array((1., 1., 1.)))
prt2.RK4_trajectory(0.01)

electron = prt.Particle(-1, 1, B_prom, np.array((0, 0, 0)), np.array((1., 1., 1.)))
electron.RK4_trajectory(0.01)

positron = prt.Particle(1, 1, B_prom, np.array((0, 0, 0)), np.array((1., 1., 1.)))
positron.RK4_trajectory(0.01)


fig = plt.figure()
axs = plt.axes(projection='3d')
axs.plot3D(prt1.x, prt1.y, prt1.z, label = 'Konstantno B')
axs.plot3D(prt2.x, prt2.y, prt2.z, label = 'Promjenjivo B')
plt.legend(loc = 'upper right')
plt.show()

fig = plt.figure()
axs = plt.axes(projection='3d')
axs.plot3D(electron.x, electron.y, electron.z, label = 'Elektron')
axs.plot3D(positron.x, positron.y, positron.z, label = 'Pozitron')
plt.legend(loc = 'upper right')
plt.show()

