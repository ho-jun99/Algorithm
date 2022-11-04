import math

n = int(input())

dp = [0 for i in range(max(n+1,6))]
dp[0] = 0
dp[1] = dp[2] = -1
dp[3] = dp[5] = 1
dp[4] = -1

# print(dp)
if n < 6 :
  # print(dp)
  print(dp[n])
  exit()
else :
  for i in range(6,n+1):
    _3 = dp[i-3]
    _5 = dp[i-5]
    if _3 != -1 and _5 == -1 :
      dp[i] = _3 +1
    elif _3 == -1 and _5 !=-1 :
      dp[i] = _5 +1
    elif _3 == -1 and _5 == -1 :
      dp[i] = -1
    else :
      dp[i] = min(_3,_5) + 1

# print(dp)
print(dp[n])



