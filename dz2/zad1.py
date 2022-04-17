import matplotlib.pyplot as plt
import numpy as np
import num_rac as nr

m=10
tmax=15

def ho(v,x,t):
	k=2
	return -k*x

def force_const(v,x,t):
	const=2
	return const

for i in range(2):
	if i:
		(t,x,v,a)=nr.move(ho,m,tmax,x0=10)
	else:
		(t,x,v,a)=nr.move(force_const,m,tmax)
	plt.figure(figsize=(10,5))

	plt.subplot(1,3,1)
	plt.plot(t,x,color='blue')
	plt.xlabel("t[s]")
	plt.ylabel("x[m]")

	plt.subplot(1,3,2)
	plt.plot(t,v,color='blue')
	plt.xlabel("t[s]")
	plt.ylabel("v[m/s]")

	plt.subplot(1,3,3)
	plt.plot(t,a,color='blue')
	plt.xlabel("t[s]")
	plt.ylabel("a[m/s^2]")

	plt.tight_layout()
	plt.show()	
		