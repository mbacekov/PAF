#include <iostream>

void jed_prav(float x1, float y1, float x2, float y2){
	if(x1 != x2){
		float a = (y2-y1)/(x2-x1);
		float b = y1 - a*x1;
		if (b<0){
			std::cout <<"Jednadzba pravca je y="<<a<<"x-"<<abs(b)<< std::endl;
		}
		else{
			std::cout <<"Jednadzba pravca je y="<<a<<"x+"<<b<< std::endl;
		}
	}
	else{
		std::cout <<"Jednadzba pravca je x="<<x1<< std::endl;
	}
}

int main(){
	float x1=4, y1=3, x2=6, y2=5;
	jed_prav(x1, y1, x2, y2);
	return 0;
}

