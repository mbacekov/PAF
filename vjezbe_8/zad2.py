import particle as prt
import matplotlib.pyplot as plt

p1 = prt.Particle(0, 0, 15, 45, 1, 1, 1, 0.2)
x1, y1 = p1.putanja(dt = 0.01)
plt.plot(x1,y1, color='g', label = 'Eulerova metoda')

p2 = prt.Particle(0, 0, 15, 45, 1, 1, 1, 0.2)
x2, y2 = p2.RK4_putanja(dt = 0.01)
plt.plot(x2,y2, color ='b', label = 'Runge-Kutta metoda') 

plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.legend(loc='upper right')
plt.grid()
plt.show()
