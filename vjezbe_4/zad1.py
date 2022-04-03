import calculus as calc
import matplotlib.pyplot as plt
import numpy as np

def kub(x):
	return x*x*x

def der_kub(x):
	return 3*x*x


lin=np.linspace(1,2)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.plot(lin, der_kub(lin),label="Analiticko rj.")
plt.xlabel("$x$")
plt.ylabel("Derivacija od $x^3$")

for i in range(3):
	(x_num,der_num)=calc.metoda2(kub,1,2,0.01*10**i)
	plt.plot(x_num,der_num, label="Numericko rj.")

plt.legend()	


plt.subplot(1,2,2)
plt.plot(lin, np.cos(lin),label="Analiticko rj.")
plt.xlabel("$x$")
plt.ylabel("Derivacija funkcije $sin(x)$")

for i in range(3):
	(x_num,der_num)=calc.metoda2(np.sin,1,2,0.01*10**i)
	plt.plot(x_num,der_num, label="Numericko rj.")

plt.legend()
plt.tight_layout()
plt.show()












