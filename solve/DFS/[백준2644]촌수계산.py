import sys
from collections import deque

n = int(sys.stdin.readline()) # 전체 사람의 수
a,b = map(int,sys.stdin.readline().split()) # 촌수를 계산해야하는 a,b
m = int(sys.stdin.readline()) # 관계의 개수

ddict = [ [] * 1 for _ in range(n+1)] # 인접리스트 만들기
visit = [False] * (n+1)

for i in range(m) :
  x,y = map(int,sys.stdin.readline().split())
  ddict[x].append(y)
  ddict[y].append(x)

## BFS (성공) ##
## start a, target b
# dq = deque()
# dq.append((a,0))
# visit[a] = True
#
# while len(dq) != 0 :
#   cur = dq.popleft() # ( 현재값, 카운터 )
#
#   for item in ddict[cur[0]] :
#     next = (item, cur[1] + 1)
#
#     if visit[next[0]] == False :
#       if next[0] == b :
#         print(next[1])
#         exit()
#       else :
#         visit[next[0]] = True # 방문처리
#         dq.append(next) # 큐에 넣기
#
# print(-1)
### --------------- ###




#
# DFS를 이용한 풀이
# a -> b를 찾기
# 시작은 a,  target은 b가 됨
#
def dfs(a,cnt) :

  if a==b :
    return cnt

  re = -1
  for next in ddict[a] :
    if not visit[next] :
      visit[next] = True
      re = max(dfs(next,cnt+1),re)

  return re

visit[a] = True
result = dfs(a,0)
if  result== None :
  print(-1)
else :
  print(result)