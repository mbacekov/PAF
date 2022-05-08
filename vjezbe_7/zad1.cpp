#include <iostream>
#include <Particle.h>

using namespace std;

float d1, t1, d2, t2;

int main(){
	Particle p1(15, 30, 0, 0);
	d1=p1.range();
	t1=p1.time();
	cout << "Domet prvog tijela je " << d1 << " metara." << std::endl;
	cout << "Vrijeme leta prvog tijela je " << t1 << " sekundi." << std::endl;

	Particle p2(5, 45, 0, 0);
	d2=p2.range();
	t2=p2.time();
	cout << "Domet drugog tijela je " << d2 << " metara." << std::endl;
	cout << "Vrijeme leta drugog tijela je " << t2 << " sekundi." << std::endl;

	return 0;
}