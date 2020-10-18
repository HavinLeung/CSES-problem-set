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

void dfs(int i, long running, long& min, int n, vector<int> v){
  if (i >= n) {
    min = std::min(min, abs(running));
  } else {
    dfs(i+1, running + v[i], min, n, v);
    dfs(i+1, running - v[i], min, n, v);
  }
}

int main() {
  int n;
  cin >> n;
  vector<int> weights;
  read_many(n, weights);
  long min = pow(10, 9) + 1;
  dfs(0, 0, min, n, weights);
  cout << min << endl;
}
