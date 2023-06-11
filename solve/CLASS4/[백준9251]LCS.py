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

# # 시간 초과 풀이 ( 리컬전 에러 ) #
# def lcs(a_idx, b_idx):
#   global a, b
#   if a_idx == -1 or b_idx == -1:
#     return 0
#   if a[a_idx] == b[b_idx]:
#     return lcs(a_idx - 1, b_idx - 1) + 1
#   else:
#     return max(lcs(a_idx - 1, b_idx), lcs(a_idx, b_idx - 1))
#
# result = lcs(len(a) - 1, len(b) - 1)
# print(result)

