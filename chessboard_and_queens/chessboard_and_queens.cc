#include <iostream>
#include <vector>
#include <set>
#include <array>
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

char v[8][8];
set<array<int, 2> > used;
int numWays;

bool can_use(int row, int col){
  if (v[row][col] == '*') {
    return false;
  }
  for (const auto& [r, c]: used) {
    if (r == row || c == col) {
      return false;
    } else if (abs(row - r) == abs(col - c)) {
      return false;
    }
  }
  return true;
}

void dfs(int row, const int n){
  if (row >= n) {
    return;
  } 
  for (int i = 0; i < n; ++i) {
    if (can_use(row, i)) {
      if (row == n-1) {
        numWays +=1;
      }
      used.insert(array{row, i});
      dfs(row+1, n);
      used.erase(array{row, i});
    }
  }
}

int main() {
  string in;
  for (int i = 0; i < 8; ++i){
    cin >> in;
    for (int j = 0; j < 8; ++j) {
      v[i][j] = in[j];
    }
  }
  dfs(0, 8);
  cout << numWays << endl;
}
