import harmonic_oscillator2 as ho
import matplotlib.pyplot as plt

p1 = ho.HarmonicOscillator()
p1.init(1, 5, 5, 0.01, 10)

p2 = ho.HarmonicOscillator()
p2.init(1, 5, 5, 0.05, 10)

p3 = ho.HarmonicOscillator()
p3.init(1, 5, 5, 0.25, 10)

p1.period()
p2.period()
p3.period()

p_an = ho.HarmonicOscillator()
p_an.init(1, 5, 5, 0.005, 10)

t, x, v, a = p1.putanja()
t2, x2, v2, a2 = p2.putanja()
t3, x3, v3, a3 = p3.putanja()
t_an, x_an, v_an, a_an = p_an.analitical()

plt.scatter(t, x, s=2, label='dt=0.01')
plt.scatter(t2, x2, s=2, label='dt=0.05')
plt.scatter(t3, x3, s=2, label='dt=0.15')
plt.plot(t_an, x_an, label='analytical')
plt.xlabel('t[s]')
plt.ylabel('x[m]')
plt.legend(loc="lower right")
plt.grid()
plt.show()

plt.scatter(t, v, s=2, label='dt=0.01')
plt.scatter(t2, v2, s=2, label='dt=0.05')
plt.scatter(t3, v3, s=2, label='dt=0.25')
plt.plot(t_an, v_an, label='dt=analitical')
plt.xlabel('t[s]')
plt.ylabel('v[m/s]')
plt.legend(loc="lower right")
plt.grid()
plt.show()

plt.scatter(t, a, s=2, label='dt=0.01')
plt.scatter(t2, a2, s=2, label='dt=0.05')
plt.scatter(t3, a3, s=2, label='dt=0.15')
plt.plot(t_an, a_an, label='dt=analitical')
plt.xlabel('t[s]')
plt.ylabel('a[m/s^2]')
plt.legend(loc="lower right")
plt.grid()
plt.show()