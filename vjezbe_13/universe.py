import numpy as np

G = 6.67408 * 10 **(-11)

class Planet:
	def __init__(self, m, r, v, radius=0):
		self.m = m
		self.r = r
		self.v = v
		self.F = 0
		self.x = [self.r[0]]
		self.y = [self.r[1]]
		self.radius = radius

class Universe:
	def __init__(self):
		self.planets = []
		self.t = 0

	def add_planet(self, Planet):
		self.planets.append(Planet)

	def __move(self):
		for glavni in self.planets:
			glavni.F = 0
			for sporedni in self.planets:
				if glavni != sporedni:
					glavni.F += -G * glavni.m * sporedni.m * (glavni.r - sporedni.r) / (np.linalg.norm(glavni.r - sporedni.r))**3
					if np.linalg.norm(glavni.r - sporedni.r) < (glavni.radius + sporedni.radius):
						print("collision")
						break

			glavni.a = glavni.F / glavni.m
			glavni.v += glavni.a * self.dt
			glavni.r += glavni.v * self.dt
			glavni.x.append(glavni.r[0])
			glavni.y.append(glavni.r[1])
		self.t += self.dt

	def trajectory(self, vrijeme, dt):
		self.dt = dt

		while self.t < vrijeme:
			self.__move()




	
	