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

	def total_time(self):
		time=0
		while(self.y[len(self.y)-1]>=self.y[0]):
			self.__move()
			time+=self.dt
		return time

	def max_speed(self):
		while(self.y[len(self.y)-1]>=self.y[0]):
			self.__move()
		v=[]
		for i in range(0,len(self.vx)):
			v.append(np.sqrt(self.vx[I]**2+self.vy[y]**2))
		max_speed=np.max(v)
		return max_speed

	def velocity_to_hit_target(self,kut_st,target_x,target_y,r):
		for v_0 in np.arange(0,100,0.01):
			self.set_initial_conditions(v_0,kut_st,0,0,0.01)
			while(self.y[len(self.y)-1]>=self.y[0]):
				self.__move()
				if np.sqrt((self.x[len(self.x)-1]-target_x)**2+(self.y[len(self.y)-1])**2) <=r:
					return v_0
			self.reset()

	def angle_to_hit_target(self,v_0,target_x,target_y,r):
		for kut_st in np.arange(0,90,0.01):
			self.set_initial_conditions(v_0,kut_st,0,0,0.01)
			while(self.y[len(self.y)-1]>=self.y[0]):
				self.__move()
				if np.sqrt((self.x[len(self.x)-1]-target_x)**2+(self.y[len(self.y)-1])**2) <=r:
					return kut_st
			self.reset()
		








