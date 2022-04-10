import matplotlib.pyplot as plt
import numpy as np
import harmonic_oscillator as ho

h1=ho.HarmonicOscillator()
m=5
k=2
x0=3
v0=10

period_num=[]
period_an=[]
step=[]

for i in np.arange(0.001,0.01,0.05):
	h1.set_initial_conditions(m,k,x0,v0,15,i)
	step.append(i)
	period_num.append(h1.period())
	period_an.append(2*np.pi/np.sqrt(k/m)) 
	h1.reset()

plt.figure(figsize=(12,6))
plt.plot(step, period_num, color='red')
plt.plot(step, period_an, color='blue')
plt.xlabel("dt[s]")
plt.ylabel("T[s]")

plt.tight_layout()
plt.show()