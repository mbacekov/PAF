import matplotlib.pyplot as plt
import math
import numpy as np

class HarmonicOscillator:

	def __init__(self):
		self.a = []
		self.v = []
		self.x = []
		self.t = []

	def init(self, m, k, x0, v0, dt=0.001):
		self.m = m
		self.k = k
		self.a.append(-(self.k/self.m)*x0)
		self.v.append(v0)
		self.x.append(x0)
		self.dt = dt
		self.t.append(0)

		self.period_an = 2*np.pi/np.sqrt(k/m)

		self.name = "HarmonicOscillator_" + str(m) + "_" + str(k)
	
		
	def reset(self):
		self.a.clear()
		self.v.clear()
		self.x.clear()
		self.t.clear()

	def get_x(self):
		return self.t, self.x

	def get_v(self):
		return self.t, self.v

	def get_a(self):
		return self.t, self.a

	def __move(self, i):
		self.t.append(self.t[i-1] + self.dt)
		self.a.append(-(self.k/self.m)*self.x[i-1])
		self.v.append(self.v[i-1]+self.a[i]*self.dt)
		self.x.append(self.x[i-1]+self.v[i]*self.dt)

	def oscillate(self, time):
		Nstep = int(time/self.dt)
		for i in range(1, Nstep):
			self.__move(i)
			
			

	def plot_trajectory(self):

		plt.figure(figsize=(12,6))

		plt.subplot(1,3,1)
		plt.scatter(self.t,self.x,s=0.5)
		plt.xlabel("t[s]")
		plt.ylabel("x[m]")

		plt.subplot(1,3,2)
		plt.scatter(self.t,self.v,s=0.5)
		plt.xlabel("t[s]")
		plt.ylabel("v[m/s]")

		plt.subplot(1,3,3)
		plt.scatter(self.t,self.a,s=0.5)
		plt.xlabel("t[s]")
		plt.ylabel("a[m/s^2]")

		plt.tight_layout()
		plt.show()

#fali numericko racunanje perioda titranja







