#include <iostream>
#include <ctime>
#include <vector>
#include <fstream>
using namespace std;

int main() {
	int n;
	fstream f("27B.txt");
	f >> n;
	
	vector <int> a(n);
	for(int i = 0; i < n; i++) f >> a[i];
	
	long long max_sum = 0;
	
	for(int i = 0; i < n; i++) {
		long long s = 0;
		for(int j = i; j < n; j++) {
			s += a[j];
			if(s % 1000 == 0 and s > max_sum) {
				max_sum = s;
			}
		}
	}
	cout << max_sum;
	return 0;
}
