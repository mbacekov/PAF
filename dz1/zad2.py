import particle as prt
import matplotlib.pyplot as plt
import numpy as np

p1=prt.Particle()

domet=[]
vrijeme=[]

for i in np.arange(0,90,0.1):
	p1.set_initial_conditions(10,i,0,0,0.01)
	vrijeme+=[p1.total_time()]
	p1.set_initial_conditions(10,i,0,0,0.01)
	domet+=[p1.range()]

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.plot(np.arange(0,90,0.1), domet)
plt.xlabel("$kut(stupnjevi)$")
plt.ylabel("$domet[m]$")

plt.subplot(1,2,2)
plt.plot(np.arange(0,90,0.1), vrijeme)
plt.xlabel("$kut(stupnjevi)$")
plt.ylabel("$t[s]$")

plt.tight_layout()
plt.show()




