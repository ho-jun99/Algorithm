import sys

a = list(" " + sys.stdin.readline().strip())
b = list(" " + sys.stdin.readline().strip())

dp = [[0] * (len(b)) for _ in range(len(a))]

for a_idx in range(1,len(a)) :
  for b_idx in range(1,len(b)) :
    if a[a_idx] == b[b_idx] :
      dp[a_idx][b_idx] = dp[a_idx-1][b_idx-1] + 1
    else :
      dp[a_idx][b_idx] = max(dp[a_idx-1][b_idx],dp[a_idx][b_idx-1])

# print2D(dp)
result = dp[-1][-1]
print(result)