import math


while True:
    try:
        x1=float(input("Unesite koord. x1 prve tocke: "))
    except ValueError:
        print('Krivi unos, probajte ponovno!')
        continue
    else:
        break

while True:
    try:
        y1=float(input("Unesite koord. y1 prve tocke: "))
    except ValueError:
        print('Krivi unos, probajte ponovno!')
        continue
    else:
        break
    
    
while True:
    try:
        x2=float(input("Unesite koord. x2 druge tocke: "))
    except ValueError:
        print('Krivi unos, probajte ponovno!')
        continue
    else:
        break

while True:
    try:
        y2=float(input("Unesite koord. y2 druge tocke: "))
    except ValueError:
        print('Krivi unos, probajte ponovno!')
        continue
    else:
        break
        
        

if (x2-x1)==0:
	print("Ovo je vertikalni pravac. Jednadzba pravca je: x=", x1)

elif (y2-y1)==0:
	print("Ovo je horizontalni pravac. Jednadzba pravca je: y=", y1)

else:
	k=((y2-y1)/(x2-x1))
	b=y1-(k*x1)
	print("Jednadzba pravca je: y=",k,"x +",b)







