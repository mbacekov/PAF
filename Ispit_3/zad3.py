import bullet as bt
import matplotlib.pyplot as plt

p1 = bt.Bullet(2, 100)

x, y, t = p1.putanja(0.01)

plt.plot(x, y)
plt.grid()
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.show()

plt.plot(t, x)
plt.grid()
plt.xlabel("t[s]")
plt.ylabel("x[m]")
plt.show()

plt.plot(t, y)
plt.grid()
plt.xlabel("t[s]")
plt.ylabel("y[m]")
plt.show()