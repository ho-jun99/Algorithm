import sys

n,k = map(int,sys.stdin.readline().split())

coins = list()
for _ in range(n) :
  coins.append(int(sys.stdin.readline().strip()))
coins.sort(reverse=True)

cnt = 0
step = 0
# print(coins)
while k > 0 :
  if k // coins[step] > 0 :
    cnt += k // coins[step]
    k = k%coins[step]
  step+=1

print(cnt)



"""
  
  # print(coins)
  dp = [float('inf')] * int(k+1)
  dp[0] = 0
  
  for i in range(1,k+1) :
    for coin in coins :
      if i - coin >= 0 :
        dp[i] = min(dp[i-coin],dp[i])
    dp[i] +=1
  
  # print(dp)
  print(dp[k])
"""