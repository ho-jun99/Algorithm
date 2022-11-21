t = int(input())

dp = [0] * (t+1)
blocks = [1,2]
dp[1] = 1



if t < 2 :
  print(dp[t])
else :
  dp[2] = 3
  for i in range(3,t+1):
    sum = 0
    for block in blocks:
      if ( i - block >= 0) :
        if (block == 2) :
          sum += 2*dp[i-block]
        else :
          sum += dp[i-block]
    dp[i] = sum % 10_007

  print(dp[t] % 10_007)