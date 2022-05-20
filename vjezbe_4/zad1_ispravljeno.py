import calculus_ispravljeno as calc
import matplotlib.pyplot as plt
import numpy as np

def kub(x):
	return x*x*x

def der_kub(x):
	return 3*x*x


fig = plt.figure(figsize=(20,10))

#Plotanje analitickog rjesenja derivacije kubne fje
x_a = np.linspace(-2,2,100)

plt.subplot(1,2,1)
plt.plot(x_a, der_kub(x_a),label="Analiticko rj.")
plt.xlabel('x')
plt.ylabel('Derivacija od $x^3$')
plt.legend()

#Plotanje numerickog rjesenja derivacije kubne fje
fx, x = calc.derivate_over_range(kub,-2,2,0.1,method=2)
plt.scatter(x,fx,s=5)


x.clear()
fx.clear()
fx, x = calc.derivate_over_range(kub,-2,2,0.01,method=2)
plt.scatter(x,fx,s=5)

plt.xlabel('x')
plt.ylabel('Derivacija od $x^3$')
plt.title('Numerical derivation')

#derivacija funkcije sinus analiticki
plt.subplot(1,2,2)
plt.plot(x_a, np.cos(x_a),label="Analiticko rj.")
plt.xlabel('x')
plt.ylabel('Derivacija od $sin(x)$')
plt.legend()

#Plotanje numerickog rjesenja za sinus
fx, x = calc.derivate_over_range(np.sin,-2,2,0.1,method=2)
plt.scatter(x,fx,s=5)


x.clear()
fx.clear()
fx, x = calc.derivate_over_range(np.sin,-2,2,0.01,method=2)
plt.scatter(x,fx,s=5)

plt.xlabel('x')
plt.ylabel('Derivacija od $sin(x)$')
plt.title('Numerical derivation')

fig.savefig('zad1_derivacija.pdf')
plt.show()

	















