import numpy as np
import matplotlib.pyplot as plt
		

def lineFromPoints(points, save = False, saveName=""):
	if (points[0][0]-points[1][0])==0:
		print("Ovo je vertikalni pravac. Jednadzba pravca je: x=", points[0][0])

	elif (points[0][1]-points[1][1])==0:
		print("Ovo je horizontalni pravac. Jednadzba pravca je: y=", points[0][1])
	else:
		k = ((points[1][1]-points[0][1])/(points[1][0]-points[0][0]))
		b = points[0][1]-(k*points[0][0])
		print("Jednadzba pravca je: y={0:.2f}x+{1:.2f}".format(k,b))

	# Prepare figure and axis
	fig = plt.figure()
	ax = plt.axes()

	# Draw line and optimize axis range
	x = np.linspace(min(points[0][0],points[1][0]) - 0.2*abs(min(points[0][0],points[1][0])), max(points[0][0],points[1][0]) + 0.2*abs(max(points[0][0],points[1][0])), 1000)
	ax.plot(x, k*x+b)

	#Draw two points as red circles
	plt.plot(points[0][0], points[0][1], marker='o', markersize=3, color='red')
	plt.plot(points[1][0], points[1][1], marker='o', markersize=3, color='red')

	#Show or save figure
	if(save):
		fig.savefig("{}.pdf".format(saveName))
	else:
		plt.show()

 
points = [[5.,2.5],[7.,3.0]]
lineFromPoints(points, True, "pravac")



