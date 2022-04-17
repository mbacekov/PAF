def move(f,m,tmax,x0=0,v0=0,t0=0,dt=0.01):

	dt=tmax/1000
	x=[x0]
	v=[v0]
	t=[t0]
	a=[f(v0,x0,t0)/m]

	while t[-1]<tmax:
		t+=[t[-1]+dt]
		x+=[x[-1]+v[-1]*dt]
		v+=[v[-1]+a[-1]*dt]
		a+=[f(v[-1],x[-1],t[-1])/m]
	return x,v,a,t