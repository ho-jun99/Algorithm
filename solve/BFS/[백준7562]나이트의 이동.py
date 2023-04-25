import sys
from collections import deque

tc = int(sys.stdin.readline())

dirs = [
  (-2,1), (-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)
  ]


def solve() :
  l = int(sys.stdin.readline()) # 체스판의 한변의 길이 l * l
  visit = [ [False] * l  for i in range(l)]
  start = tuple(map(int,sys.stdin.readline().split())) # 현재 말의 위치
  target = tuple(map(int,sys.stdin.readline().split())) # 나이트가 가야할 위치
  dq = deque()
  dq.append( (start[0],start[1],0) ); visit[start[0]][start[1]] = True

  while len(dq) != 0 :
    cur = dq.popleft()
    # 현재 위치가 타겟이랑 같은지 확인
    if cur[0] == target[0] and cur[1] == target[1] :
      print(cur[2])
      return

    for dir in dirs :
      next = ( cur[0] + dir[0], cur[1] + dir[1], cur[2] + 1 )
      if 0<= next[0] < l and 0<= next[1] < l : # 이동이 체스보드안이라면
        if visit[next[0]][next[1]] == False : # 방문했던 곳이 아니라면
          #방문하기
          dq.append(next)
          visit[next[0]][next[1]] = True

          if next[0] == target[0] and next[1] == target[1]:
            print(next[2])
            return




for _ in range(tc) :
  solve()