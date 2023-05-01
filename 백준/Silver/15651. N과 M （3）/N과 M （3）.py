import sys

N,M = map(int,sys.stdin.readline().split())

targets = [i for i in range(1,N+1)]

# 중복순열의 문제
def dfs(mstr,cnt) :
  global M
  if cnt == M+1 :
    print(mstr)
    return

  for target in targets :
    next = mstr + str(target) + " "
    dfs(next,cnt+1)


dfs("",1)
