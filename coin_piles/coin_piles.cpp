#include <iostream>

using namespace std;

int main() {
  int t, a, b;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cin >> a >> b;
    if (a > b) swap(a,b);
    if (a*2 < b) {
      cout << "NO" << endl;
    } else {
      if ((a+b)%3 == 0) {
        cout << "YES" << endl;
      } else {
        cout << "NO" << endl;
      }
    }
  }
}