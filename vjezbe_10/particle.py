import numpy as np

class Particle:
	def __init__(self, q, m, B, E, v0, position, t_uk, dt):
		self.q = q
		self.m = m
		self.B = B
		self.E = E
		self.position = [position]
		self.t_uk = t_uk
		self.dt = dt
		self.v = [v0]
		self.t = [0]
		self.a = [(self.q/self.m) * (self.E + np.cross(self.v[-1], self.B))]

	def move(self):
		while self.t[-1] <= self.t_uk:
			self.a.append((self.q/self.m) * (self.E + np.cross(self.v[-1], self.B)))
			self.v.append(self.v[-1] + self.a[-1] * self.dt)
			self.position.append(self.position[-1] + self.v[-1] * self.dt)
			self.t.append(self.t[-1] + self.dt)


	def akc_RK4(self,v):
		return (self.q/self.m) * (self.E + np.cross(v, self.B))

	def move_RK4(self):
		while self.t[-1] <= self.t_uk:
			k1v = self.akc_RK4(self.v[-1]) * self.dt
			k1_position = self.v[-1] * self.dt

			k2v = self.akc_RK4(self.v[-1] + k1v/2) * self.dt
			k2_position = (self.v[-1] + (k1_position/2)) * self.dt

			k3v = self.akc_RK4(self.v[-1] + k2v/2) * self.dt
			k3_position = (self.v[-1] + (k2_position/2)) * self.dt

			k4v = self.akc_RK4(self.v[-1] + k3v) * self.dt
			k4_position = (self.v[-1] + (k3_position)) * self.dt

			self.v.append( self.v[-1] + (k1v + 2*k2v + 2*k3v + k4v)/6)
			self.position.append(self.position[-1] + (k1_position + 2*k2_position + 2*k3_position + k4_position)/6)

			self.t.append(self.t[-1] + self.dt)

	def coord(self):
		x = []
		y = []
		z = []

		for position in self.position:
			x.append(position[0])
			y.append(position[1])
			z.append(position[2])

		return x, y, z






