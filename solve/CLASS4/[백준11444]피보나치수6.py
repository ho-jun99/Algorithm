import sys

n = int(sys.stdin.readline().strip())
REMAINDER = 1_000_000_007

# 제곱을 구하는 분할정복
def power(adj, n):
  if n == 1:
    return adj
  elif n % 2:
    return multi(power(adj, n - 1), adj)
  else:
    return power(multi(adj, adj), n // 2)


# 행렬의 곱셈
def multi(a, b):
  temp = [[0] * len(b[0]) for _ in range(2)]
  for i in range(2):
    for j in range(len(b[0])):
      sum = 0
      for k in range(2):
        sum += a[i][k] * b[k][j]
      temp[i][j] = sum % REMAINDER
  return temp


# 초기 행렬
adj = [[1, 1], [1, 0]]
# 피보나치 초기값
start = [[1], [1]]
if n < 3:
  print(1)
else:
  print(multi(power(adj, n - 2), start)[0][0])

# # 메모리를 적게 사용하는 DP 풀이 (시간초과) --
# dp = [0,1,1]
#
# idx = 3
# if n<= 2 :
#   print(dp[n])
# else :
#   while idx <= n :
#     dp[idx%3] = (dp[(idx-1)%3] + dp[(idx-2)%3]) % REMAINDER
#     idx+=1
#
# print(dp[n%3])
