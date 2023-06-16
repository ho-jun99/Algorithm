import sys
from collections import deque

def print2D(arr):
  for i in arr :
    print(i)
  print()

N,M = map(int,sys.stdin.readline().split())

# 로봇 청소기 위치, 바라보는 방향
r,c,d = map(int,sys.stdin.readline().split())

board = list()

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# 반시계 방향으로 회전한다.
dirs = [
  (-1,0),(0,1),(1,0),(0,-1)
  ]


for _ in range(N) :
  line = list(map(int,sys.stdin.readline().split()))
  board.append(line)

# 0 = 청소되지 않은 빈 칸
# 1 = 벽

cnt = 0
visit = [[False] * M for _ in range(N)]
dq = deque()
dq.append((r,c,d))

while len(dq) != 0 :
  r,c,d = dq.pop()
  # print("dq : ", dq)

  # 방문처리를 진행한다.
  if board[r][c] == 0 and visit[r][c] == False :
    cnt +=1
    visit[r][c] = True
    # print(r,c,d)
    # print2D(visit)

  canGo = False
  for i in range(1,5) :
    nd = (d-i) % 4 # 다음방향을 결정한다.
    dir = dirs[nd]
    nr = r + dir[0]; nc = c + dir[1]

    if 0 < nr < N and 0 < nc < M : # 이동이 가능하면
      if visit[nr][nc] == False and board[nr][nc] == 0 : # 이동 가능한 조건이다.
        dq.append( (nr,nc,nd) )
        # print(nr, nc, nd)
        canGo = True
        break

  if not canGo :
    bd = (d+2) % 4 #후진방향
    dir = dirs[bd]
    br = r + dir[0]; bc = c + dir[1]

    if (0 < br < N and 0 < bc < M ) and board[br][bc] == 0:
      dq.append((br,bc,d)) # 후진이동
      # print("back")
    else :
      break

print(cnt)




