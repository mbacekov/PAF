#include <iostream>

void kruznica(float sx, float sy, float r, float x, float y){
	if ((x-sx)*(x-sx)+(y-sy)*(y-sy) < r*r){
		std::cout <<"Tocka se nalazi unutar kruznice."<< std::endl;
	}
	else if ((x-sx)*(x-sx)+(y-sy)*(y-sy) > r*r){
		std::cout <<"Tocka se nalazi izvan kruznice."<< std::endl;
	}
}

int main(){
	float sx=2, sy=2, r=1, x=1, y=0;
	kruznica(sx, sy, r, x, y);
	return 0;
}