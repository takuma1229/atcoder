#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N;
  cin >> N;

  vector<int> points(N);
  for (int i = 0; i < N; i++)
  {
    int point;
    cin >> point;
    points.at(i) = point;
  }

  // とりあえず平均を計算
  int sum = 0;
  for (int i = 0; i < N; i++)
  {
    sum += points.at(i);
  }
  int average = sum / N;

  for (int i = 0; i < N; i++)
  {
    int dif = abs(average - points.at(i));
    cout << dif << endl;
  }
}