import sys


def solve(num):
  dp = [0] * int(11 + 1)
  dp[1] = 1
  dp[2] = 2
  dp[3] = 4

  for i in range(4, num + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
  # print(dp)
  print(dp[num])


t = int(sys.stdin.readline())
for _ in range(t):
  num = int(sys.stdin.readline())
  solve(num)
