import numpy as np
import matplotlib.pyplot as plt

class Pendulum:
	def __init__(self, kut_st, l, m):

		self.kut_st = kut_st
		self.l = l
		self.m = m
		self.t = [0]
		self.theta0 = self.kut_st*np.pi/180
		self.theta = [self.theta0]
		

		if self.kut_st < 10:
			print("Unesen je mali kut od {} stupnjeva.".format(self.kut_st))
		else:
			print("Molimo unesite kut manji od 10 stupnjeva.")


	def reset(self):
		self.t = [0]
		self.theta0 = self.kut_st*np.pi/180
		self.theta = [self.theta0]

	def change_theta(self, m, th):
		if m == 2:
			self.theta0 = th
			print("Unjeli ste kut u radijanima iznosa {}.".format(self.theta0))
		if m == 3:
			self.kut_st = th
			print("Unjeli ste kut u stupnjevima iznosa {}.".format(self.kut_st))


	def __move(self):
		g = -9.81
		self.t.append(self.t[-1] + self.dt)
		self.w0 = self.theta0 * (-g/self.l) * self.dt
		self.w.append(self.w[-1] - self.theta[-1]*self.dt*(g/self.l))
		self.theta.append(self.theta[-1] + self.w[-1]*self.dt)

	def putanja(self, dt, T):
		self.dt = dt
		self.T = T
		while self.t[-1] < self.T:
				self.__move()
		return self.t, self.theta


	def plot_trajectory(self):
		plt.plot(self.t, self.theta)
		plt.xlabel("t[s]")
		plt.ylabel("theta")
		plt.show()


