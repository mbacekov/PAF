#include <iostream>

void zamjena(int polje[], int prvi, int drugi){
	int x = polje[prvi];
	polje[prvi] = polje[drugi];
	polje[drugi] = x;
}

void okretanje(int polje[], int size){
	int polje2[size];
	
	for (int i = 0; i < size; i++)
		polje2[i]=polje[size-i-1];

	for (int i=0; i < size; i++)
		polje[i]=polje2[i];
}

void sortiranje(int polje[], int size){
	for (int i = 0; i < size; i++){
		for (int j = i+1; j < size; j++){
			if (polje[i] > polje[j]){
				zamjena(polje, i, j);
			}
		}
	}
}

int main(){
	int polje[8] = {2,3,5,7,11,13,17,19}, a=1, b=15;

	std::cout << "U intervalu [" << a << "," << b << "] nalaze se: "<< std::endl;

	for (int i=0; i < 8; i++)
		if (polje[i] >= a && polje[i] <= b)
			std::cout << polje[i] << " " << std::endl;

	zamjena(polje, 1, 2);
	okretanje(polje, 8);
	sortiranje(polje, 8);
	return 0;
}
	