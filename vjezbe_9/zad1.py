import bungee as bng
import numpy as np
import matplotlib.pyplot as plt

#l, m, k, ro, Cd, A, h0
jump1 = bng.Bungee(25, 60, 75, 1, 1, 1, 100)
jump1.plot_trajectory()

jump2 = bng.Bungee(25, 60, 75, 1, 0, 1, 100)
jump2.plot_trajectory()

