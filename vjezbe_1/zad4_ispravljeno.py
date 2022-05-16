#creating an empty list
points = [[] for i in range(2)]

#Read coordinates of a point
def read_coordinates(point, i):
	x1 = float(input("Unesite x koordinatu {}. tocke: ".format(i+1)))
	points[i].append(x1)

	y1 = float(input("Unesite y koordinatu {}. tocke: ".format(i+1)))
	points[i].append(y1)

		

def lineFromPoints(points):
    
    if (points[0][0]-points[1][0])==0:
	    print("Ovo je vertikalni pravac. Jednadzba pravca je: x=", points[0][0])

    elif (points[0][1]-points[1][1])==0:
        print("Ovo je horizontalni pravac. Jednadzba pravca je: y=", points[0][1])

    else:
        k = ((points[1][1]-points[0][1])/(points[1][0]-points[0][0]))
        b = points[0][1]-(k*points[0][0])
        print("Jednadzba pravca je: y={0:.2f}x+{1:.2f}".format(k,b))

 
for i in range(0,2):
	read_coordinates(points, i) 

lineFromPoints(points)
