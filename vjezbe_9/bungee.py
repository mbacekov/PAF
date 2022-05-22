import numpy as np
import matplotlib.pyplot as plt

class Bungee:
	def __init__(self, l, m, k, ro, Cd, A, h0):
		self.l = l
		self.m = m
		self.k = k	
		self.ro = ro
		self.Cd = Cd
		self.A = A
		self.h0 = h0
		self.v = [0]
		self.t = [0]
		self.y = [h0]
		self.dt = 0.01
		self.a = [-9.81]
		self.Eel = [0]
		self.Ek = [0]
		self.Ep = [h0 * m * 9.81]
		self.Euk = []

	def __akc_bez_Fel(self, v, y):
		return -9.81 - np.sign(v)*(self.ro * self.Cd * self.A) / (2*self.m) *v**2

	def __akc_s_Fel(self, v, y):
		return -9.81 - np.sign(v)*(self.ro * self.Cd * self.A) / (2*self.m) *v**2 + self.k/self.m * (self.h0 - self.y[-1] - self.l)

	def __kin(self, m, v):
		return m*v**2/2

	def __pot(self, m, h):
		return m*h*9.81

	def __elast(self, k, x):
		return k*x**2/2

	def __move(self, a):
		self.a.append(a(self.v[-1], self.y[-1]))
		self.v.append(self.v[-1] + self.a[-1] * self.dt)
		self.y.append(self.y[-1] + self.v[-1] * self.dt)
		self.t.append(self.t[-1] + self.dt)
		self.Ek.append(self.__kin(self.m, self.v[-1]))
		self.Ep.append(self.__pot(self.m, self.y[-1]))

	def plot_trajectory(self):
		while self.t[-1] < 50:
			if self.y[-1] > self.h0 - self.l:
				self.__move(self.__akc_bez_Fel)
				self.Eel.append(0)

			else:
				self.__move(self.__akc_s_Fel)
				self.Eel.append(self.__elast(self.k, self.h0 - self.y[-1] - self.l))

		plt.plot(self.t, self.y, label='dt=0.01 Runge-Kutta')
		plt.xlabel('t[s]')
		plt.ylabel('y[m]')
		plt.legend()
		plt.show()

		for i in range(len(self.Eel)):
			self.Euk.append(self.Ek[i] + self.Eel[i] + self.Ep[i])

		plt.plot(self.t, self.Ek, label='kinetic energy')
		plt.plot(self.t, self.Ep, label='potential energy')
		plt.plot(self.t, self.Eel, label='elastic energy')
		plt.plot(self.t, self.Euk, label='total energy')
		plt.xlabel("t[s]")
		plt.ylabel("E[J]")
		plt.legend()
		plt.show()








