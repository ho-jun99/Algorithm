# 100번칸을 넘어가면 이동X
# 뱀이 있는 칸에 도착 -> 내려감, 사다리 칸에 도착 -> 올라감
# 1번칸 시작 100번칸 도착
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().strip().split())

ladders = []

adj = [ -1 for i in range(0,101)]

for i in range(n+m) : # 사다리
  a,b = map(int,sys.stdin.readline().strip().split())
  adj[a] = b
  ladders.append((a,b))

dq = deque()
cur = (1,1,0)
visit = [False for i in range(101)]
dq.append(cur) # 1에서 시작
dirs = [1,2,3,4,5,6]

while len(dq) > 0 :
  # print(cur,end=" -> ")
  cur = dq.popleft()
  if cur[0] == 100 :
    print(cur[2])
    break
  for dir in dirs :
    next = cur[0] + dir
    if 0<= next <= 100 and not visit[next]:
      temp = (0,0,0)
      if adj[next] != -1 :
        temp = (adj[next], cur[0],cur[2]+1)
      else :
        temp = (next, cur[0], cur[2] +1 )
      visit[temp[0]] = True
      dq.append(temp)
      if temp[0] == 100 :
        print(temp[2])
        exit()