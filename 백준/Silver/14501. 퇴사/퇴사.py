import sys


def print2D(arr) :
  for i in arr:
    print(i)
  print()

N = int(sys.stdin.readline())
t = [0] * (N+1)
p = [0] * (N+1)

for i in range(1,N+1) :
  time,pay = map(int,sys.stdin.readline().split())
  t[i] = time
  p[i] = pay

dp = [0] * (N+2)

for i in range(N,-1,-1) :
  if i + (t[i]-1) <= N :
    dp[i] = max(dp[i+1] ,dp[i+(t[i])] + p[i])
  else :
    dp[i] = dp[i+1]

print(dp[0])