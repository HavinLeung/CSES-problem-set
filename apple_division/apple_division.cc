#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

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
  for (int i = 0; i < n; ++i) {
    int tmp;
    cin >> tmp;
    weights.push_back(tmp);
  }
  long min = pow(10, 9) + 1;
  dfs(0, 0, min, n, weights);
  cout << min << endl;
}