class Bullet:
	def __init__(self, h, vx):
		self.h = h
		self.vx0 = vx
		self.t = [0]
		self.x = [self.t[-1]*self.vx0]
		self.y = [self.h]
		self.vx = [self.vx0]
		self.vy = [0]
		print("Objekt je uspjesno stvoren. Visina je jednaka {} m, a brzina {} m/s.".format(h, vx))

#ovako bi trebala izgledati privatna metoda, nije mi radilo, pa sam dodala print neovisno o njoj 

		def __provjera(self):
			print("Objekt je uspjesno stvoren. Visina je jednaka {} m, a brzina {} m/s.".format(h, vx))

	def reset(self):
		self.x = [self.t[-1]*self.vx0]
		self.y = [self.h]
		self.vx = [self.vx0]
		self.vy = [0]
		self.t = [0]

	def change_h(self, dh):
		self.h += dh

	def change_vx(self, dvx):
		self.vx0 += dvx

	def __move(self):
		a = -9.81
		self.t.append(self.t[-1] + self.dt)
		self.vx.append(self.vx[-1])
		self.x.append(self.x[-1] + self.vx[-1]*self.dt)
		self.vy.append(self.vy[-1] + a*self.dt)
		self.y.append(self.y[-1] + self.vy[-1]*self.dt)

	def putanja(self, dt):
		self.dt = dt
		while (self.y[-1]>=0):
			self.__move()
		return self.x, self.y, self.t	


#beskonacno vrti petlju...	


	def meta(self, s1, s2, dy, h, dt):
		self.h = h
		self.dt = dt
		self.s1 = s1
		self.s2 = s2
		self.dy = dy
		self.vx0 = 0.5
		y1 = s2 - dy
		y2 = s2 + dy
		pogodak = False
		while pogodak == False:
			self.putanja(self.dt)
			if self.x[-1] == s1 and self.y[-1]>=y1 and self.y[-1] <= y2:
				pogodak = True
				print("Meta je pogodena!")
				vx0_pogodak = self.vx0
			else:
				self.reset()
				self.vx0 += 0.5
				self.vx = [self.vx0]
		return vx0_pogodak, self.x, self.y, self.t, self.s1, self.s2, self.dy


#utjecaj vjetra se racuna kao utjecaj na akceleraciju u x-smjeru

	def __move_vjetar(self):
		ay = -9.81
		self.t.append(self.t[-1] + self.dt)
		self.vx.append(self.vx[-1] + self.ax*self.dt)
		self.x.append(self.x[-1] + self.vx[-1]*self.dt)
		self.vy.append(self.vy[-1] + ay*self.dt)
		self.y.append(self.y[-1] + self.vy[-1]*self.dt)


	def putanja_vjetar(self, dt):
		self.dt = dt
		while (self.y[-1]>=0):
			self.__move_vjetar()
		return self.x, self.y, self.vy, self.t



#ista stvar kao i gornja petlja

	def meta_vjetar(self, s1, s2, dy, h, dt, vjetar):
		self.ax = vjetar
		self.h = h
		#self.dt = dt
		self.s1 = s1
		self.s2 = s2
		self.dy = dy
		#self.vx0 = 0.5
		y1 = s2 - dy
		y2 = s2 + dy
		pogodak = False
		while pogodak == False:
			self.putanja_vjetar(0.1)
			if self.x[-1] == s1 and self.y[-1]>=y1 and self.y[-1] <= y2:
				pogodak = True
				print("Meta je pogodena!")
				vx0_pogodak = self.vx0
			else:
				self.reset()
				self.vx0 += 0.5
				self.vx = [self.vx0]
		return vx0_pogodak, self.x, self.y, self.t









