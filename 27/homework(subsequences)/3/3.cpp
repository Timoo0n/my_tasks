#include <iostream>
#include <vector>
#include <fstream>
#include <ctime>
using namespace std;

int main() {
	int n;
	fstream f("27B.txt");
	f >> n;
	
	vector <int> l(n);
	for(int i = 0; i < n; i++) f >> l[i];
	
	long long count = 0;
	for(int i = 0; i < n; i++) {
		long long k = 0;
		for(int j = i; j < n; j++) {
			if (l[j] % 5 == 0) k++;
			if (k % 11 == 0) count++;
		}
	}
	cout << count << endl;
	cout << clock();
	return 0;
}
