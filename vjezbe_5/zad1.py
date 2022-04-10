import matplotlib.pyplot as plt
import numpy as np
import harmonic_oscillator as ho

h1=ho.HarmonicOscillator()
h2=ho.HarmonicOscillator()

h1.set_initial_conditions(5,2,3,10,0.01,15) #m,k,x0,v0,dt,t
h1.plot_trajectory()
h1.reset()
h1.set_initial_conditions(5,2,3,10,0.01,15)
t1,x1,v1,a1=h1.oscillator_data()
h1.reset()
h1.set_initial_conditions(5,2,3,10,0.01,15)


h2.set_initial_conditions(5,2,3,10,0.03,15)
t2,x2,v2,a2=h2.oscillator_data()

def fun(t):
	return 3*np.cos(np.sqrt(2/5)*t)+(10/np.sqrt(2/5))*np.sin(np.sqrt(2/5)*t) #x0*cos(omega*t)+(v0/omega)*sin(omega*t)

xan=[]
for i in t1:
	xan.append(fun(i))

plt.figure(figsize=(12,6))
plt.plot(t1,xan, color='red')
plt.scatter(t1,x1,s=8,color='yellow')
plt.scatter(t2,x2,s=8,color='blue')
plt.xlabel("t[s]")
plt.ylabel("x[m]")

plt.tight_layout()
plt.show()










