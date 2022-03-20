import matplotlib.pyplot as plt
import numpy as np

def jednoliko_gibanje(T,F,m,x_0,v_0):
	
	x=[x_0]
	v=[v_0]
	T=T
	a=F/m
	N=10000
	dt=T/N
	N=int(N)

	for i in range(N):
		v+=[v[i]+a*dt]
		x+=[x[i]+v[i+1]*dt]

	t=np.linspace(0,T,N+1)

	plt.figure(figsize=(10,6))

	plt.subplot(2,2,1)
	plt.plot(t,x)
	plt.title("Polozaj")
	plt.xlabel("$t[s]$")
	plt.ylabel("$x[m]$")

	plt.subplot(2,2,2)
	plt.plot(t,v)
	plt.title("Brzina")
	plt.xlabel("$t[s]$")
	plt.ylabel("$v[m/s]$")

	plt.subplot(2,2,3)
	plt.plot(t,len(t)*[a])
	plt.title("Akceleracija")
	plt.xlabel("$t[s]$")
	plt.ylabel("$a[m/s^2]$")

	plt.tight_layout()
	plt.show()

def kosi_hitac(T,v_0,kut_st):
	theta=kut_st*np.pi/180
	g=-9.81
	T=T
	N=10000
	dt=T/N
	N=int(N)

	x=[0.]
	y=[0.]
	v_x=[v_0*np.cos(theta)]
	v_y=[v_0*np.sin(theta)]


	for i in range(N):
		v_x+=[v_x[0]]
		v_y+=[v_y[i]+g*dt]
		x+=[x[i]+v_x[i+1]*dt]
		y+=[y[i]+v_y[i+1]*dt]

	t=np.linspace(0,T,N+1)

	plt.figure(figsize=(10,6))

	plt.subplot(2,2,1)
	plt.plot(x,y)
	plt.title("Putanja cestice x-y")
	plt.ylabel("$y[m]$")
	plt.xlabel("$x[m]$")

	plt.subplot(2,2,2)
	plt.plot(t,x)
	plt.title("Koordinata x u vremenu")
	plt.xlabel("$t[s]$")
	plt.ylabel("$x[m]$")

	plt.subplot(2,2,3)
	plt.plot(t,y)
	plt.title("Koordinata y u vremenu")
	plt.xlabel("$t[s]$")
	plt.ylabel("$y[m]$")

	plt.tight_layout()
	plt.show()





