import matplotlib.pyplot as plt
import numpy as np

F=10.
m=2.
T=10.
a=F/m
N=10000
dt=T/N
N=int(N)

x=[0.]
v=[0.]

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






	
