import particle as prt
import matplotlib.pyplot as plt

p1 = prt.Particle(0, 0, 15, 45, 1, 1, 1, 0.2)
x1, y1 = p1.putanja(dt = 0.01)
plt.plot(x1,y1, color='g', label='dt=0.01')
plt.xlabel('x[m]')
plt.ylabel('y[m]') 

p2 = prt.Particle(0, 0, 15, 45, 1, 1, 1, 0.2)
x2, y2 = p2.putanja(dt = 0.005)
plt.plot(x2,y2, color ='b', label='dt=0.005') 
plt.xlabel('x[m]')
plt.ylabel('y[m]')

p3 = prt.Particle(0, 0, 15, 45, 1, 1, 1, 0.2)
x3, y3 = p3.putanja(dt = 0.05)
plt.plot(x3,y3, color='r', label='dt=0.05') 
plt.xlabel('x[m]')
plt.ylabel('y[m]')

plt.legend(loc='upper right')
plt.grid()
plt.show()

print("Za dt manji od 0.01 Eulerova metoda ne daje naznake nefizikalnog gibanja.")