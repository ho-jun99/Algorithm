import math
import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
if n < 4 :
  print(n)
  exit()

dp[1] = 1; dp[2] = 2; dp[3] = 3;
for i in range(4,n+1) :
  target = int(math.sqrt(i))
  if ( i == target**2) :
    dp[i] = 1
  else :
    my_min = 4
    while target > 0 :
        my_min = min(my_min, 1 + dp[i-(target**2)])
        target = target-1
    dp[i] = my_min
print(dp[n])