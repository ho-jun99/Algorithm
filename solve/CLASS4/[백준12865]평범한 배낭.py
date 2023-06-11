import sys

def print2D(arr) :
  for i in arr :
    print(i)
  return

N,K = map(int,sys.stdin.readline().split())
arr = list()

for _ in range(N) :
  weight, value = map(int,sys.stdin.readline().split())
  arr.append((weight,value))

dp = [[0] * (K+1) for _ in range(N+1)]

# 주요 풀이 방법은, 물건들의 범위를 하나씩 늘려간다
  # 이때 해당 물건까지 사용 할 수 있다는 조건이 생기게 된다.

for i in range(1,N+1) :
  arridx = i-1
  weight, value = arr[arridx]
  for j in range(K+1) :
    if weight <= j :
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight] + value) # 안담을때, 담을때
    else :
      dp[i][j] = dp[i-1][j] # 복사해가기

# print2D(dp)
print(dp[N][K])

# ## Fraction Knapsack 풀이 방법이다 ##
# arr.sort(key=lambda x : (-x[0],x[1],-x[2]))
# print(arr)
# idx = 0
# result = 0
# while K > 0 :
#   print(result,idx)
#   wv, weight, value = arr[idx]
#   if K - weight >= 0 :
#     result += value
#     K -= weight
#   idx+=1
#   if K <= 0 or idx >= len(arr):
#     break
#
# print(result)

