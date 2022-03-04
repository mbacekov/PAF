import math
x='x'
x1=float(input('Upisite koordinatu x prve tocke: '))
y1=float(input('Upisite koordinatu y prve tocke: '))
x2=float(input('Upisite koordinatu x druge tocke: '))
y2=float(input('Upisite koordinatu y druge tocke: '))
k=(y2-y1)/(x2-x1)
b=k*x1+y1
y=k*x-b
print ('Jednadzba pravca iznosi y= ',y)




