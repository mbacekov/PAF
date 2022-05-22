import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1=prt.Particle(0, 0, 60, 45, 1, 1, 0.2, oblik=1, dimenzija=0.1)
p1.angle_to_hit_target(15,15,0.1)
print("Projektil pogada metu ako ga izbacimo pod kutem od {:.2f} stupnjeva.".format(p1.theta))


p2=prt.Particle(0, 0, 60, 45, 1, 1, 0.2, oblik=1, dimenzija=0.1)
p2.angle_to_hit_target(7,15,0.1)
print("Projektil pogada metu ako ga izbacimo pod kutem od {:.2f} stupnjeva.".format(p2.theta))



target1 = plt.Circle((p1.xm, p1.ym), p1.r, color ='r')
target2 = plt.Circle((p2.xm, p2.ym), p2.r, color ='b')
fig, axs = plt.subplots()
axs.set_aspect("equal")
axs.add_patch(target1)
axs.add_patch(target2)
axs.plot(p1.x, p1.y)
axs.plot(p2.x, p2.y)
plt.setp(axs, xlabel='x[m]')
plt.setp(axs, ylabel='y[m]')
plt.grid()
plt.show()