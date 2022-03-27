import particle as prt
import numpy as np

p1=prt.Particle()
p1.set_initial_conditions(26, 45, 0, 0, 0.01)

num_rj=p1.range()
an_rj=p1.v_0**2/9.81*np.sin(2*p1.th)

def err(num_rj, an_rj):
	return (np.abs(num_rj-an_rj)/an_rj)*100

error=err(num_rj, an_rj)

print("Numericko rjesenje dometa je {:.3f} m.".format(num_rj))
print("Analiticko rjesenje dometa je {:.3f} m.".format(an_rj))
print("Odstupanje numerickog i analitickog dometa je {:.3f} m.".format(error))