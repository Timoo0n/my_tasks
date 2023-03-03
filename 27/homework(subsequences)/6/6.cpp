#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
	int n;
	fstream f("27_B.txt");
	f >> n;
	
	vector <long long> l(n);
	for(int i = 0; i < n; i++) f >> l[i];
	
	long long length = 0;
	long long max_sum = 0;
	
	for(int i = 0; i < n; i++) {
		long long s = 0;
		long long c = 0;
		for(int j = i; j < n; j++) {
			s += l[j];
			c++;
			if(s % 69 == 0 and s > max_sum) {
				max_sum = s;
				length = c;
			}
			
		}
	}
	cout << length;
	
	return 0;
}
