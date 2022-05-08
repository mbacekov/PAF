#include <iostream>

class Particle{
	private:
		double t, x, y, vx, vy;
		double g = -9.81;
		double dt = 0.0001;

		void evolve();

	public:
		Particle(double v0, double theta, double x0, double y0);

		double time();
		double range();

};