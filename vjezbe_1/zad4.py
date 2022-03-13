def lineFromPoints(P, Q):
    
    if (Q[0]-P[0])==0:
	    print("Ovo je vertikalni pravac. Jednadzba pravca je: x=", P[0])

    elif (Q[1]-P[1])==0:
        print("Ovo je horizontalni pravac. Jednadzba pravca je: y=", P[1])

    else:
        k = ((Q[1]-P[1])/(Q[0]-P[0]))
        b = P[1]-(k*P[0])
        print("Jednadzba pravca je: y= ",k,"x +",b)

 
 
P = [float(x) for x in input("Unesite koord. tocke P: ").split()]
Q = [float(x) for x in input("Unesite koord. tocke Q: ").split()]
 

lineFromPoints(P, Q)
