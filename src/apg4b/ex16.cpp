#include <bits/stdc++.h>
using namespace std;

int main()
{
  vector<int> vec(5);
  for (int i = 0; i < 5; i++)
  {
    cin >> vec.at(i);
  }

  bool flag = false;
  for (int i = 1; i < 5; i++)
  {
    if (vec.at(i - 1) == vec.at(i))
    {
      flag = true;
    }
  }

  if (flag)
  {
    cout << "YES" << endl;
  }
  else
  {
    cout << "NO" << endl;
  }
}