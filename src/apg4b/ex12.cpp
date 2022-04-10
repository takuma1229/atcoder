#include <bits/stdc++.h>
using namespace std;

int main()
{
  string S;
  cin >> S;

  int ans = 1;

  // ここにプログラムを追記
  for (int i = 0; i < (S.size() / 2); i++)
  {
    string p_or_m;
    p_or_m = S.at(2 * i + 1);

    if (p_or_m == "+")
    {
      ans++;
      // cout << "plus" << endl;
    }
    else
    {
      ans--;
      // cout << "minus" << endl;
    }
  }
  cout << ans << endl;
}
