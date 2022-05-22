import numpy as np

class Particle:
	def __init__(self, x0, y0, v0, theta, rho, Cd, m, oblik, dimenzija):
		if oblik == 1:
			self.A = np.pi*dimenzija**2
		elif oblik == 2:
			self.A = dimenzija**2
		else:
			print("Krivo upisan oblik, upisite 1 za kuglu ili 2 za kocku.")
		self.x0 = x0
		self.y0 = y0
		self.v0 = v0
		self.theta = theta
		self.rho = rho
		self.Cd = Cd
		self.m = m
		self.x = [x0]
		self.y = [y0]
		self.t = [0]
		self.vx = [v0*np.cos(theta*np.pi/180)]
		self.vy = [v0*np.sin(theta*np.pi/180)]
		self.ay = [-9.81-(self.rho*self.Cd*self.A)/(2*self.m)*self.vy[-1]*abs(self.vy[-1])]
		self.ax = [-(self.rho*self.Cd*self.A)/(2*self.m)*self.vx[-1]*abs(self.vx[-1])]

	def reset(self):
		self.x = [self.x0]
		self.y = [self.y0]
		self.t = [0]
		self.vx = [self.v0*np.cos(self.theta*np.pi/180)]
		self.vy = [self.v0*np.sin(self.theta*np.pi/180)]
		self.ay = [-9.81-(self.rho*self.Cd*self.A)/(2*self.m)*self.vy[-1]*abs(self.vy[-1])]
		self.ax = [-(self.rho*self.Cd*self.A)/(2*self.m)*self.vx[-1]*abs(self.vx[-1])]

	def __move(self):
		self.t.append(self.t[-1] + self.dt)
		self.ay.append(-9.81-(self.rho*self.Cd*self.A)/(2*self.m)*self.vy[-1]*abs(self.vy[-1]))
		self.ax.append( -(self.rho*self.Cd*self.A)/(2*self.m)*self.vx[-1]*abs(self.vx[-1]))
		self.vy.append( self.vy[-1] + self.ay[-1]*self.dt)
		self.vx.append( self.vx[-1] + self.ax[-1]*self.dt)
		self.y.append( self.y[-1] + self.vy[-1]*self.dt)
		self.x.append( self.x[-1] +self.vx[-1]*self.dt)

	def putanja(self, dt):
		self.dt = dt
		while self.y[-1]>=0:
			self.__move()
		return self.x, self.y

	def RK4_ax(self, v, x=0, t=0):
		return -v*abs(v)*(self.rho*self.Cd*self.A)/(2*self.m)

	def RK4_ay(self, v, x=0, t=0):
		return -9.81-v*abs(v)*(self.rho*self.Cd*self.A)/(2*self.m)

	def __RK4_move(self):
		k1vy = self.RK4_ay(self.vy[-1]) * self.dt
		k1vx = self.RK4_ax(self.vx[-1]) * self.dt
		k1y = self.vy[-1] * self.dt
		k1x = self.vx[-1] * self.dt

		k2vy = self.RK4_ay(self.vy[-1] + k1vy/2) * self.dt
		k2vx = self.RK4_ax(self.vx[-1] + k1vx/2) * self.dt
		k2y = (self.vy[-1] + (k1vy/2)) * self.dt
		k2x = (self.vx[-1] + (k1vx/2)) * self.dt

		k3vy = self.RK4_ay(self.vy[-1] + k2vy/2) * self.dt
		k3vx = self.RK4_ax(self.vx[-1] + k2vx/2) * self.dt
		k3y = (self.vy[-1] + (k2vy/2)) * self.dt
		k3x = (self.vx[-1] + (k2vx/2)) * self.dt

		k4vy = self.RK4_ay(self.vy[-1] + k3vy) * self.dt
		k4vx = self.RK4_ax(self.vx[-1] + k3vx) * self.dt
		k4y = (self.vy[-1] + (k3vy)) * self.dt
		k4x = (self.vx[-1] + (k3vx)) * self.dt

		self.vy.append( self.vy[-1] + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6)
		self.vx.append( self.vx[-1] + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6)
		self.y.append(self.y[-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)
		self.x.append(self.x[-1] + (k1x + 2*k2x + 2*k3x + k4x)/6)

	def RK4_putanja(self, dt):
		self.dt = dt
		while self.y[-1]>=0:
			self.__RK4_move()
		return self.x, self.y

	def angle_to_hit_target(self, xm, ym, r, dt=0.01):
		self.xm = xm
		self.ym = ym
		self.r = r
		self.dt = dt
		self.theta = 0
		hit = False
		for i in range(1000):
			self.reset()
			while self.y[-1]>=0:
				self.__RK4_move()
				if (self.x[-1] - xm)**2 + (self.y[-1] - ym)**2 <= r**2:
					hit = True
					break
			if hit == True:
				break
			self.theta += 0.1
		if hit == False:
			print("Premalena brzina da bi meta bila pogodena.")
			quit()





		
	
		