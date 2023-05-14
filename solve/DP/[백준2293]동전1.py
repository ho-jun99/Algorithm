'''
  - 동전2와 다르게 경우의 수를 구하는 문제이다.
'''
import sys

coins = list()
n, k = map(int, sys.stdin.readline().split())
for _ in range(n):
  coin = int(sys.stdin.readline().strip())
  coins.append(coin)

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins :
  for i in range(coin,k+1) :
    dp[i] = dp[i] + dp[i-coin]
    print(dp)
print(dp[k])


