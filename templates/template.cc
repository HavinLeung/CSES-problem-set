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

template <class T>
void read_matrix(int m, int n, vector <vector <T> >& v) {
  for (int i = 0; i < m; ++i) {
    vector<T> vi;
    read_many(n, vi);
    v.push_back(vi);
  }
}

int main() {
}
