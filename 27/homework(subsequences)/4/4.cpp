#include <iostream>
#include <vector>
#include <ctime>
#include <fstream>
using namespace std;
//Уверенно пишем перебор на плюсах
int main() {
	int n;
	fstream f("27_B.txt");
	f >> n;
	
	vector <long long> l(n);
	for(int i = 0; i < n; i++) f >> l[i];
	
	long long max_sum = 0;
	
	for(int i = 0; i < n; i++) {
		long long k = 0;
		long long s = 0;
		for(int j = i; j < n; j++) {
			s += l[j];
			if (l[j] % 5 == 0) k ++;
			if (k % 3 == 0 && max_sum < s) {
				max_sum = s;
			} 
		}
	}
	cout << max_sum;
	return 0;
}
