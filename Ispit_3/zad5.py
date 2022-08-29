import bullet as bt
import matplotlib.pyplot as plt

p1 = bt.Bullet(2, 0.5)
p2 = bt.Bullet(2, 0.5)

vx0, x1, y1, t, s1, s2, dy= p1.meta(50, 1.5, 0.1, 0.05, 2)

vx0, x2, y2, t, s1, s2, dy= p2.meta_vjetar(50, 1.5, 0.1, 0.05, 2, -3)

plt.plot(p1.s1, p1.s2)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.axis(equal)
plt.grid()
plt.show()