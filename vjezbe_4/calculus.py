def metoda1(fun,x,dx,met=3):
	if met==2:
		return (fun(x+dx)-fun(x))/dx
	else:
		return (fun(x+dx)-fun(x-dx))/2*dx

def metoda2(fun,a,b,dx,met=3):
	x=[]
	d=[]
	for i in range(int((b-a)/dx)+1):
		x+=[a+i*dx]
		d+=[metoda1(fun,x[i],dx,met)]
	return x,d

def int_prav(fun,a,b,N):
	dx=(b-a)/N
	gornja=0
	donja=0

	for i in range(0,N):
		gornja+=fun(a+(i+1)*dx)
		donja+=fun(a+i*dx)
	
	return gornja*dx, donja*dx

def int_trap(fun,a,b,N):
	dx=(b-a)/N
	int=(fun(a)+fun(b))/2

	for i in range(0,N):
		int+=fun(a+i*dx)
	
	return int*dx
	