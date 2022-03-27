import numpy as np
import matplotlib.pyplot as plt

class Particle:
	def __init__(self):
		self.x=[]
		self.y=[]
		self.vx=[]
		self.vy=[]
		self.ax=0
		self.ay=-9.81

	def set_initial_conditions(self, v_0, kut_st, x_0, y_0, dt):
		self.v_0=v_0
		self.dt=dt
		self.th=kut_st*np.pi/180
		self.x+=[x_0]
		self.y+=[y_0]
		self.vx+=[v_0*np.cos(self.th)]
		self.vy+=[v_0*np.sin(self.th)]

	def reset(self):
		self.x=[]
		self.y=[]
		self.vx=[]
		self.vy=[]

	def __move(self):
		self.vx+=[self.vx[len(self.vx)-1]+self.ax*self.dt]
		self.vy+=[self.vy[len(self.vy)-1]+self.ay*self.dt]
		self.x+=[self.x[len(self.x)-1]+self.vx[len(self.vx)-1]*self.dt]
		self.y+=[self.y[len(self.y)-1]+self.vy[len(self.vy)-1]*self.dt]

	def range(self):
		while(self.y[len(self.y)-1]>=self.y[0]):
			self.__move()
		domet=self.x[len(self.x)-1]
		return domet

	def plot_trajectory(self):
		while(self.y[len(self.y)-1]>=self.y[0]):
			self.__move()
		plt.plot(self.x, self.y)
		plt.xlabel("$x(m)$")
		plt.ylabel("$y(m)$")
		plt.show()








