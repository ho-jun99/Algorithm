from itertools import combinations
import sys

n,m = map(int,sys.stdin.readline().split())
arr = [i for i in range(1,n+1)]

# nCm
# n! / (n-r)! * r!
# DP 로 팩토리얼을 구하자

mulit = 1
cnt = 2
dp = [-1] * 101
dp[1] = 1
while True :
  if cnt == n+1 :
    break
  dp[cnt] = dp[cnt-1]*cnt
  cnt+=1

print(dp[n] // ((dp[n-m]) * dp[m]))