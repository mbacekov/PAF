import matplotlib.pyplot as plt
import numpy as np

def save_or_show():
    inp = input("Izaberite prikaz pravca ili spremanje u pdf")
    if inp == "prikaz pravca":
    	plt.show()
    elif inp == "spremanje u pdf":
	fname=input("Izaberite naziv pdf dokumenta:")
	plt.savefig(fname, format='pdf', bbox_inches='tight')
    else:
	print("Morate izabrati jednu od 2 opcije")
	return save_or_show()

P = [float(x) for x in input("Unesite koord. tocke P: ").split()]
Q = [float(x) for x in input("Unesite koord. tocke Q: ").split()]


x_values = [[P[0], Q[0]]]
y_values = [[P[1], Q[1]]]

plt.plot(x_values, y_values, marker='o', color = 'blue', linewidth=1)

save_or_show()


