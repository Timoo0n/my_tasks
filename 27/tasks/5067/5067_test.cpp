#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
using namespace std;

int main() {
	int n;
	ifstream f("27-B.txt");
	f >> n;
	
	vector <int> a(n);
	
	for(int i=0; i < n; i++) f >> a[i];
	
	long long count = 0;
	
	for(int i = 0; i < n; i++) {
		for(int j = i+1; j < n; j++) {
			if ((a[i]+a[j]) % 3 == 0 && (a[i]*a[j]) % 4096 == 0) count++;
		}
	}
	cout << count << endl;
	cout << clock();
}

