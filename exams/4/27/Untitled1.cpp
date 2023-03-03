#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
	int n; // кол-во
	fstream f("27B.txt");
	f >> n;
	
	vector <int> l(n);
	for(int i=0; i<n; i++) f>>l[i];
	
	long long ln = 0;
	for(int i=0; i<n; i++) {
		long long c1 = 0;
		long long c2 = 0;
		for(int j=i; j<n; j++) {
			 
			if (l[j] % 2 == 0) c2++;
			else if (l[j] % 2 == 1) c1++;
			if (c2==c1) ln = max(c1+c2, ln); 
			
		}
	}
	cout << ln;
	return 0;
}
