#include <iostream>

using namespace std;

int main() {
  long n, count = 0;
  cin >> n;
  for(long i = 5; (n/i) >= 1; i*=5) {
    count += n / i;
  }
  cout << count << endl;
}