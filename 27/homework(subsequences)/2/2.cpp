#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main() {
	int n;
	fstream f("27B.txt");
	f >> n;
	
	vector <int> l(n);
	for(int i = 0; i < n; i++) f >> l[i];
	
	long long count = 0;
	
	for(int i = 0; i < n; i ++) {
		long long s = 0;
		for(int j = i; j < n; j++) {
			s += l[j];
			if (s % 666 == 0) count ++;
			
		}
	}
	cout << count;
	
	return 0;
}
