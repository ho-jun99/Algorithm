'''
  - DP배열을 -1로 초기화 해주는게 좋을 듯 하다.
    - 만일 중간에 0인 지점이 있을텐데 그 지점은 못와서 0일텐데 이걸 체크 안하면 그다음은 여기에 1더해버리기 때문이다.
    - 문제에서 나름 불가능할경우 -1을 출력하라는거에서 힌트처럼 느껴질수도..
'''
import sys

coins = list()
n,k = map(int,sys.stdin.readline().split())
for _ in range(n) :
  coin = int(sys.stdin.readline().strip())
  coins.append(coin)

dp = [-1] * (k+1) # 메모이제이션을 위한 배열
dp[0] = 0

for i in range(k+1) :
  minimum = float('inf')
  for coin in coins :
    before = i - coin
    if 0 <= before and dp[before] != -1:
      minimum = min(minimum, dp[before] + 1)
      dp[i] = minimum

print(dp[k])