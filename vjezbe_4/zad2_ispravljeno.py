import calculus_ispravljeno as calc
import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return 2*x**2 + 3

analitical_integral = 11./3.

num_dn, num_up = calc.integrate_up_dn(f,0,1,10)
print("Donja granica: {0:} \n Gornja granica: {1:}".format(num_dn,num_up))

fig = plt.figure(figsize=(20,10))

# Plotanje numerickog rjesenja
dn = []
up = []
trapez = []
step = []

for N in np.arange(50, 1000, 50):
	num_dn, num_up = calc.integrate_up_dn(f,0,1,N)
	dn.append(num_dn)
	up.append(num_up)
	trapez.append(calc.integrate(f,0,1,N))
	step.append(N)

plt.scatter(step, up, s=10)
plt.scatter(step, dn, s=10)
plt.scatter(step, trapez, s=10)

# Plotanje analitickog rjesenja


plt.axhline(y=analitical_integral,label='analiticko rj.')
plt.legend()
plt.title("Numericka integracija")
plt.xlabel("Broj podjela")
plt.ylabel("Vrijednost integracije")

fig.savefig("zad2_integracija.pdf")
plt.show()


