import matplotlib.pyplot as plt
import numpy as np

class HarmonicOscillator:
	def __init__(self):
		self.a=[]
		self.v=[]
		self.x=[]
		self.t=[0]

	def set_initial_conditions(self,m,k,x0,v0,dt,t):
		self.m=m
		self.k=k
		self.a+=[-k/m*x0]
		self.v+=[v0]
		self.x+=[x0]
		self.dt=dt
		self.t=t
	
		

	def reset(self):
		self.a=[]
		self.v=[]
		self.x=[]
		self.t=[0]

	def __move(self,t,dt=0.1):
		self.t=0
		self.N=int(self.t/dt)
		for i in self.N:
			self.a+=[(np.sqrt(self.k/self.m))**2*self.x[i-1]]
			self.v+=[self.v[i-1]+self.a[i-1]*dt]
			self.x+=[self.x[i-1]+self.v[i]*dt]
			self.t+=i*dt
			

	def plot_trajectory(self):
		
		self.__move(15)

		plt.figure(figsize=(12,6))

		plt.subplot(1,3,1)
		plt.scatter(self.t[i],self.x[i],s=8)
		plt.xlabel("t[s]")
		plt.ylabel("x[m]")

		plt.subplot(1,3,2)
		plt.scatter(self.t[i],self.v[i],s=8)
		plt.xlabel("t[s]")
		plt.ylabel("v[m/s]")

		plt.subplot(1,3,3)
		plt.scatter(self.t[i],self.a[i],s=8)
		plt.xlabel("t[s]")
		plt.ylabel("a[m/s^2]")

		plt.tight_layout()
		plt.show()


	def oscillator_data(self):
		self.t.pop(0)
		for i in self.t:
			self.__move()
		self.t.insert(0,0)
		return self.t, self.x, self.v, self.a



	



		











