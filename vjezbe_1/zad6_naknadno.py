import numpy as np
import matplotlib.pyplot as plt

def kruznica(xt, yt, xs, ys, r):
	if (xs-xt)**2 + (ys-yt)**2 > r**2:
		print("Tocka se nalazi izvan kruznice.")
	elif (xs-xt)**2 + (ys-yt)**2 < r**2:
		print("Tocka se nalazi unutar kruznice.")
	else:
		print("Tocka se nalazi na kruznici.")

	# crtanje tocke i kruznice
	plt.scatter(xt, yt, color = 'red')
	circle1 = plt.Circle((xs, ys), r, color = 'blue', fill = False)
	plt.gca().add_patch(circle1)
	plt.axis('equal')

	# ispis gdje se tocka nalazi i koliko je udaljena od kruznice
	print("Tocka se nalazi na polozaju ({0:.2f}, {1:.2f}) i udaljena je za {2:.2f} od kruznice.".format(xt, yt, np.abs(np.sqrt((xs-xt)**2 + (ys-yt)**2)-r)))

	#izbor ispisa grafa
	while True:
		try:
			graf = int(input("Ako zelite prikazati graf na ekranu upisite 1, ako ga zelite spremiti kao PDF upisite 2: "))
		except ValueError:
			print("Pogresan unos.")
			continue
		else:
			break

	if graf == 1:
		plt.show()

	if graf == 2:
		plt.savefig(input("Spremi kao: ") + ".pdf")



kruznica(5, 5, 1, 1, 2) #(xt, yt, xs, ys, r)