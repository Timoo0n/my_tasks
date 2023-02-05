#include <iostream>
#include <vector>
#include <ctime>
#include <fstream>
#include <cmath>
using namespace std;

int main() {
	int n;
	
	fstream f("27B.txt");
	f >> n;
	
	vector <long long> l(n);
	for(int i = 0; i < n; i++) f >> l[i];
	
	long long min_sum = pow(10, 20);
	
	for(int i = 0; i < n; i ++) {
		long long k = 0;
		long long s = 0;
		for(int j = i; j < n; j ++) {
			s += l[j];
			if (l[j] % 3 == 0) k++;
			if (k == 10 && min_sum > s) {
				min_sum = s;
			}
		}
	}
	cout << min_sum;
	return 0;
}
