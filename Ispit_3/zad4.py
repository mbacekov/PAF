import bullet as bt
import matplotlib.pyplot as plt

p1 = bt.Bullet(2, 0.5)

vx0, x, y, t, s1, s2, dy= p1.meta(50, 1.5, 0.1, 0.01, 2)
print("Metak ce pogoditi metu, s vremenskim intervalom 0.01s, ako ga ispucamo brzinom {:.2f} m/s.".format(vx0))

vx0, x, y, t, s1, s2, dy= p1.meta(50, 1.5, 0.1, 0.05, 2)
print("Metak ce pogoditi metu, s vremenskim intervalom 0.05s, ako ga ispucamo brzinom {:.2f} m/s.".format(vx0))

vx0, x, y, t, s1, s2, dy= p1.meta(50, 1.5, 0.1, 0.1, 2)
print("Metak ce pogoditi metu, s vremenskim intervalom 0.1s, s vremenskim intervalom 0.01s, ako ga ispucamo brzinom {:.2f} m/s.".format(vx0))

