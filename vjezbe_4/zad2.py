import calculus as calc
import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return 3*x*x+6

plt.figure(figsize=(10,5))

for i in range(100,1000,50):
	plt.scatter(i,calc.int_prav(f,1,2,i)[0],c='b',label='gornja granica' if i==50 else '')
	plt.scatter(i,calc.int_prav(f,1,2,i)[1],c='r',label='donja granica' if i==50 else '')
	plt.scatter(i,calc.int_trap(f,1,2,i),c='yellow',label='trapezna integracija' if i==50 else'')
	

plt.axhline(y=13,c='green',label='analiticko rj.')
plt.legend()
plt.title("Numericka integracija $\mathrm{\int_{1}^{2}3x^2+6\ dx}$")
plt.xlabel("Broj podjela")
plt.ylabel("Vrijednost integracije")
plt.show()


