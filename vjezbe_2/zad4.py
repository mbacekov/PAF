import kosi_hitac as kh

#prva varijabla je svugdje pocetna brzina, a druga pocetni kut u odnosu na horizontalu

kh.putanja(15, 45) #plotanje putanje

h = kh.max_height(15, 45) #max visina
d = kh.hor_range(15, 45) #domet
v = kh.max_speed(15, 45, 2) #max brzina, treca varijabla je vrijeme gibanja

print("Maksimalna visina projektila je {:.4}m, domet je {:.4}m, a maksimalna brzina je {:.4}m/s.".format(h,d,v))

#plotanje gadanja mete
#zadnje 3 varijable su po redu: x koord. sredista mete, y koord. sredista mete, radijus mete

kh.target(15, 45, 10, 4, 2)
