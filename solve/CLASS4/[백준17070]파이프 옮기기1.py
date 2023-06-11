import sys

def print2D(arr) :
  for i in arr :
    print(i)

N = int(sys.stdin.readline().strip())
board = list()

for _ in range(N) :
  line = list(map(int,sys.stdin.readline().split()))
  board.append(line)

# 파이프를 계속 바꿔가면서 board를 바꾸어야 하기 때문에 백트래킹을 쓰는게 적합할거 같다

# PIPE #
PIPE_HORI = 0 # 가로
PIPE_VERT = 1 # 세로
PIPE_DIAG = 2 # 대각
HORI = [(0,1,PIPE_HORI)] # 가로
VERT = [(1,0,PIPE_VERT)] # 세로
DIAG = [(0,1,PIPE_DIAG),(1,0,PIPE_DIAG),(1,1,PIPE_DIAG)] # 대각
PIPE_DIRS = [
  [HORI,DIAG], # 가로인 경우
  [VERT,DIAG], # 세로인 경우
  [HORI,VERT,DIAG] # 대각인 경우
]
# ---- #

# 초기 상태 #
board[0][0] = -1
board[0][1] = -1
result = 0

dp = [ [0] * (N)for _ in range(N)]

if board[N-1][N-1] == 1 :
  print(0)
  exit()

def dfs(row, col, state) :
  global result,board

  checks = PIPE_DIRS[state]
  for check in checks :
    isCanGo = True
    movepoint = (-1,-1,-1)

    for dir in check :
      next = (row + dir[0] , col + dir[1])
      if 0 <= next[0] < N and 0 <= next[1] < N : # 범위 안이면서
        if board[next[0]][next[1]] == 0 : # 이동가능한 지점 0이면 이동이 가능하다
          movepoint = (next[0], next[1], dir[2])
        else :
          isCanGo = False
          break
      else :
        isCanGo = False
        break

    if isCanGo : # 이동이 가능하다면 여기서 이동을 시켜야 한다.
      # print(f"!!GO!! : {movepoint}")
      if movepoint[0] == N-1 and movepoint[1] == N-1 :
        result+=1
        return

      if movepoint[2] == PIPE_DIAG : # 대각 이동일 경우 visit를 다르게 해결해야한다.
        # 방문 처리
        board[movepoint[0]][movepoint[1]] = -1
        board[movepoint[0]-1][movepoint[1]] = -1
        board[movepoint[0]][movepoint[1]-1] = -1
        dfs(movepoint[0], movepoint[1], movepoint[2])
        board[movepoint[0]][movepoint[1]] = 0
        board[movepoint[0] - 1][movepoint[1]] = 0
        board[movepoint[0]][movepoint[1] - 1] = 0
      else :
        board[movepoint[0]][movepoint[1]] = -1 # 방문 처리
        dfs(movepoint[0],movepoint[1],movepoint[2])
        board[movepoint[0]][movepoint[1]] = 0  # 방문 처리 지우기

dfs(0,1,PIPE_HORI)
print(result)