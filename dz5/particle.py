import numpy as np

class Particle:
	def __init__(self, q, m, B, E, v):
		self.q = q
		self.m = m
		self.B = B
		self.E = E
		self.x = [0.]
		self.y = [0.]
		self.z = [0.]
		self.v = v
		self.t = [0.]

	def reset(self):
		self.x = [0.]
		self.y = [0.]
		self.z = [0.]
		self.t = [0.]


	def akc_RK4(self,v):
		return (self.q/self.m) * (self.E + np.cross(self.v, self.B(self.t)))

	def move_RK4(self):

		k1v = self.akc_RK4(self.v) * self.dt
		k1_position = self.v * self.dt

		k2v = self.akc_RK4(self.v + k1v/2) * self.dt
		k2_position = (self.v + k2v/2) * self.dt

		k3v = self.akc_RK4(self.v + k2v/2) * self.dt
		k3_position = (self.v + k2v/2) * self.dt

		k4v = self.akc_RK4(self.v + k3v) * self.dt
		k4_position = (self.v + k3v) * self.dt

		self.v += (k1v + 2*k2v + 2*k3v + k4v)/6
		self.x.append(self.x[-1] + (k1_position[0] + 2*k2_position[0] + 2*k3_position[0] + k4_position[0])/6)
		self.y.append(self.y[-1] + (k1_position[1] + 2*k2_position[1] + 2*k3_position[1] + k4_position[1])/6)
		self.z.append(self.z[-1] + (k1_position[2] + 2*k2_position[2] + 2*k3_position[2] + k4_position[2])/6)

		self.t.append(self.t[-1] + self.dt)

	def RK4_trajectory(self, dt):
		self.dt = dt
		while self.t[-1] < 10:
			self.move_RK4()






