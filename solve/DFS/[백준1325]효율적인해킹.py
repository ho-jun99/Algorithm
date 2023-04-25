import sys
from collections import defaultdict
from collections import deque


N,M = map(int, sys.stdin.readline().split())
# 1 ~ N 까지 컴퓨터의 번호가 주어짐
# M개의 줄에 신뢰하는 관계 형성

ddict = defaultdict(list)

for i in range(M) :
  a,b = map(int, sys.stdin.readline().split())
  ddict[b].append(a) # A가 B를 신뢰한다. B -> A / B를 해킹하면 A를 알 수 있다.

# ###---시간초과 -> PyPy 제출 풀이 ---###
counter = [-1] * (N+1)
mmax = 0
for index in range(1,N+1) :
  visited = [False] * (N+1)
  stk = deque()
  stk.append(index)
  visited[index] = True

  cnt = 0
  while len(stk) != 0 :
    cur = stk.pop() # 뽑기

    for next in ddict[cur] :
      if visited[next] == False :
        cnt += 1
        visited[next] = True
        stk.append(next)

  counter[index] = cnt
  mmax = max(cnt,mmax)

for index,item in enumerate(counter):
  if item == mmax :
    print(index,end=" ")


### ----- ###
# DP와 DFS를 활용해서 풀어보자
# memo = [-1] * (N+1)
# mmax = 0
# def dfs(cur) :
#   global mmax
#
#   if len(ddict[cur]) == 0 : # 맨마지막이면
#     return 1
#
#   if memo[cur] != -1 :
#     return memo[cur]
#
#   cnt = 0
#   for next in ddict[cur] :
#     cnt += dfs(next)
#
#   memo[cur] = cnt + 1
#   mmax = max(cnt+1, mmax)
#   return memo[cur]
#
# for i in range(1,N+1) :
#   dfs(i)
#   # memo[i] -= 1
#   # print(f"{i} : {memo}")
#
# for index,item in enumerate(memo) :
#   if item == mmax :
#     print(index,end=" ")
#