#include <bits/stdc++.h>
using namespace std;

int main()
{
  int A, B, C;
  cin >> A >> B >> C;

  int tallest = max({A, B, C});
  int shortest = min({A, B, C});

  cout << tallest - shortest << endl;
}