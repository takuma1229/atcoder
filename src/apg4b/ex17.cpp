#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N, S;
  cin >> N >> S;
  vector<int> A(N);
  vector<int> P(N);

  for (int i = 0; i < N; i++)
  {
    cin >> A.at(i);
  }

  for (int i = 0; i < N; i++)
  {
    cin >> P.at(i);
  }

  int count = 0;

  for (int a : A)
  {
    for (int p : P)
    {
      if (a + p == S)
      {
        count++;
      }
    }
  }

  cout << count << endl;
}