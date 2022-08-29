import bullet as bt

p1 = bt.Bullet(15, 30)
p2 = bt.Bullet(10, 45)

p1.change_h(5)
p2.change_vx(-10)

print("Nova visina prvog metka je {} m, a nova brzina drugog metka je {} m/s.".format(p1.h, p2.vx0))