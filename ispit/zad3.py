import pendulum as pd

objekt = pd.Pendulum(30, 1, 0.1)

objekt.putanja(0.01, 5)
objekt.plot_trajectory()