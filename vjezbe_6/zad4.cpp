#include <iostream>

int main(){
	float a1=1, b1=-2, c1=3, a2=2, b2=1, c2=4;

	float x,y;

	x = (c1-c2*b1/b2)/(a1-a2*b1/b2);
	y = (c1-a1*x)/b1;

	std::cout << "x = " << x << "\t y = " << y << std::endl;
}
