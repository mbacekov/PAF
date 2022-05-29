import particle as prt
import numpy as np
import matplotlib.pyplot as plt

# q, m, B, E, v0, position, t_uk, dt

prt1 = prt.Particle(-1, 1, np.array((0, 0, 1)), np.array((0, 0, 0)), np.array((0.1, 0.1, 0.1)), np.array((0, 0, 0)), 30, 0.01)
prt1.move()
x1, y1, z1 = prt1.coord()

prt2 = prt.Particle(-1, 1, np.array((0, 0, 1)), np.array((0, 0, 0)), np.array((0.1, 0.1, 0.1)), np.array((0, 0, 0)), 30, 0.01)
prt2.move_RK4()
x2, y2, z2 = prt2.coord()

fig = plt.figure()
axs = plt.axes(projection='3d')
axs.plot3D(x1, y1, z1)
axs.plot3D(x2, y2, z2, linestyle = "dashed")
plt.legend(['Euler, dt=0.01', 'Runge-Kutta, dt=0.01'])
plt.show()