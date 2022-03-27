import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1=prt.Particle()
dt=0.001

def err(num_rj, an_rj):
	return (np.abs(num_rj-an_rj)/an_rj)*100

rel_gr=[]
korak=[]

while(dt<0.1):
	p1.reset()
	p1.set_initial_conditions(10, 60, 0, 0, dt)
	num_rj=p1.range()
	an_rj=p1.v_0**2/9.81*np.sin(2*p1.th)
	rel_gr+=[err(num_rj, an_rj)]
	korak+=[dt]
	dt+=0.001


plt.plot(korak, rel_gr)
plt.xlabel("$dt[s]$")
plt.ylabel("Apsolutna relativna greska [%]")
plt.show()