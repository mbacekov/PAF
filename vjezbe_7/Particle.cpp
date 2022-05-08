#include <Particle.h>
#include <math.h>
#include <iostream>

#define pi 3.141592

void Particle::evolve(){
	vx += 0.;
	vy += g*dt;

	x += vx*dt;
	y += vy*dt;

	t += dt;
}

double Particle::range(){
	while (y >= 0){
		evolve();
	}
	return x;
}

double Particle::time(){
	while (y >= 0){
		evolve();
	}
	return t;
}

Particle::Particle(double v0, double theta, double x0, double y0)
{
	t = 0;
	x = x0;
	y = y0;

	vx = v0*cos(theta*pi/180);
	vy = v0*sin(theta*pi/180);
}