import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

PLUS = 0
MINUS = 1
MULTI = 2
DIVIDE = 3

# + - * /
temp = list(map(int,sys.stdin.readline().split()))
ops = list()
for idx,op in enumerate(temp) :
  for j in range(op) :
    ops.append(idx)

mmin = float('inf')
mmax = -float('inf')


# 연산자를 중복을 허용하지 않는 순열로 배치하면 된다.
visit = [False] * len(ops)
chosen = list()
def dfs() :
  global chosen, visit,ops,nums,mmin, mmax
  if len(chosen) == N-1 :
    # print(chosen)
    result = nums[0]
    for i in range(1,len(nums)) :
      if chosen[i-1] == PLUS :
        result = result + nums[i]
      if chosen[i-1] == MINUS :
        result = result - nums[i]
      if chosen[i-1] == MULTI :
        result = result * nums[i]
      if chosen[i-1] == DIVIDE :
        if result < 0 :
          result = -1 * (abs(result) // nums[i])
        else :
          result = result // nums[i]
      # print(i,result)
    mmin = min(result,mmin)
    mmax = max(result,mmax)
    return

  for i in range(len(ops)) :
    if not visit[i] :
      chosen.append(ops[i])
      visit[i] = True
      dfs()
      visit[i] = False
      chosen.pop()

dfs()
print(mmax)
print(mmin)
