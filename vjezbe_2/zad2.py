import matplotlib.pyplot as plt
import numpy as np

g=-9.81
T=10.
N=10000
dt=T/N
N=int(N)

def vtheta(v_0, theta):
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

v_0=26. #Sandra Perkovic disk
kut_st=45.

vtheta(v_0, kut_st*np.pi/180)



	
