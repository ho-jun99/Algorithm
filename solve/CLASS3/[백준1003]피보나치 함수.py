import sys

t = int(sys.stdin.readline())

def solve(n,dp,memo) :
  if n==0 :
    dp[0] = 0
    # memo[0] = [[1,0]]
    return 0

  elif n==1 :
    dp[1] = 1
    # memo[1] = [[0,1]]
    return 1

  else :
    if dp[n-1] == -1 :
      dp[n-1] = solve(n-1,dp,memo)
    if dp[n-2] == -1 :
      dp[n-2] = solve(n-1,dp,memo)

    dp[n] = dp[n-1]+dp[n-2]
    memo[n] = [(memo[n-1][0] + memo[n-2][0]), (memo[n-1][1] + memo[n-2][1])]
    return dp[n]

def solve2(num,memo):
  if num== 0 :
    memo[0] +=1
    return 0
  elif num == 1 :
    memo[1] +=1
    return 1
  else :
    return solve2(num-1,memo) + solve2(num-2,memo)

# 출력 형식
# 0출력횟수 1출력횟수
for _ in range(t) :
  num = int(sys.stdin.readline())
  dp = [-1]*41
  memo = [[0,0]]*41
  memo[0] = [1,0]
  memo[1] = [0,1]
  # print(solve(num,dp,memo))
  solve(num,dp,memo)
  print(memo[num][0],memo[num][1])

  # m = dict({0:0,1:0})
  # solve2(num,m)
  # print(m[0],m[1])