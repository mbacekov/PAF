import matplotlib.pyplot as plt
import math
import numpy as np

#unutar klase dodano analiticko rjesenje

class HarmonicOscillator:

	def __init__(self):
		self.a = []
		self.v = []
		self.x = []
		self.t = []

	def init(self, m, k, x0, dt, t_max):
		self.m = m
		self.k = k
		self.a.append(-(self.k/self.m)*x0)
		self.v.append(0)
		self.x.append(x0)
		self.dt = dt
		self.t.append(0)
		self.Amp = x0
		self.t_max = t_max

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

	def __move(self):
		self.t.append(self.t[-1] + self.dt)
		self.a.append(-(self.k/self.m)*self.x[-1])
		self.v.append(self.v[-1]+self.a[-1]*self.dt)
		self.x.append(self.x[-1]+self.v[-1]*self.dt)

	def putanja(self):
		while self.t[-1] < self.t_max:
			self.__move()
		return self.t, self.x, self.v, self.a

	def analitical(self):
		t_an = np.linspace(0, 10, 10000)
		for i in t_an:
			self.x.append(self.Amp*math.cos(math.sqrt(self.k/self.m)*i))
			self.v.append(-self.Amp*math.sqrt(self.k/self.m)*math.sin(math.sqrt(self.k/self.m)*i))
			self.a.append(-self.Amp*(self.k/self.m)*math.cos(math.sqrt(self.k/self.m)*i))
		del self.x[-1], self.v[-1], self.a[-1]
		return t_an, self.x, self.v, self.a
			
			

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


	def period(self):
		while self.v[-1] <= 0:
			self.__move()
		while self.v[-1] >0:
			self.__move()
		print("Period uz korak {} s je jednak {:.4f} s, analiticki period iznosi {:.4f} s. ".format(self.dt, self.t[-1], self.period_an))







