#include <iostream>

void sustav_jednadzbi(float a1, float b1, float c1, float a2, float b2, float c2){
	float x, y;
	if (a1*b2-b1*a2 == 0){
		std::cout << "Nema rjesenja.";
	}else{
		x = (c1-c2*b1/b2)/(a1-a2*b1/b2);
		y = (c1-a1*x)/b1;

		std::cout << "x = " << x << "\t y = " << y << std::endl;
	}
}
		

int main(){
	sustav_jednadzbi(2,3,4,2,-1,3);
}
