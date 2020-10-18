#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

template <class T>
void read_many(int n, vector<T>& v){
  for (int i = 0; i < n; ++i) {
    T tmp;
    cin >> tmp;
    v.push_back(tmp);
  }
}

int main() {
  int n;
  cin >> n;
}
