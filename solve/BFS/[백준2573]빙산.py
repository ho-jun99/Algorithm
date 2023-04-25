import sys
from collections import deque

# 파이썬에서 map이 어떤 역할하는지 알아보기

N, M = map(int, sys.stdin.readline().split())

board = list()

for _ in range(N) :
  line = list(map(int,sys.stdin.readline().split()))
  board.append(line)


dirs = [
  (-1,0),(0,1),(1,0),(0,-1)
  ]

def print_board() :
  for i in range(N) :
    for j in range(M) :
      print(board[i][j],end=" ")
    print()
  print()

year = 0
while True : # 여기 반복문은 1년이 증가하는 것을 표기함
  # print_board()
  visit = [ [False] * M for _ in range(N)]
  # bfs를 돌려서 빙산이 몇조각인지 확인한다.
  partition = 0
  end_cnt = 0
  for r in range(N) :
    for c in range(M) :
      if board[r][c] == 0 or visit[r][c]: # 0인곳이거나, 방문했던 곳이면 검사하지 않는다.
        if board[r][c] == 0 :
          end_cnt +=1
        continue

      partition +=1 #시작지점에서 파티션이 나뉘기 때문에 +1 시킨다.
      # print("here", f"{r} , {c}")
      dq = deque()
      dq.append((r,c))

      while len(dq) != 0 :
        cur = dq.popleft()

        for dir in dirs :
          next = (cur[0]+dir[0], cur[1]+dir[1])
          if 0<= next[0] < N and 0<= next[1] < M :
            if board[next[0]][next[1]] != 0 and visit[next[0]][next[1]] ==False: # 0이 아니고, 방문했던 곳이 아니라면
              dq.append(next) # 방문 하고
              visit[next[0]][next[1]] = True # 방문 처리를 한다.
  if end_cnt == M*N :
    print(0)
    exit()

  if partition >= 2 :
    # 2조각 이상이라면 여기서 해당 year를 출력시킨다.
    print(year)
    exit()
  else :
    # 2조각 이상이 아니라면 1년을 증가시킨다.
    year+=1
    # 1년이 증가하면 빙하가 녹아야 한다.
    meltings = list()
    for r in range(N) :
      for c in range(M) :
        if board[r][c] == 0 :
          continue

        cnt = 0
        for dir in dirs :
          next = (r + dir[0], c + dir[1])
          if board[next[0]][next[1]] == 0 :
            cnt += 1
        meltings.append((r,c,cnt))

    for item in meltings : # 하나씩이 아닌 일괄적으로 녹여야 하기 때문에
      board[item[0]][item[1]] -= item[2]
      if board[item[0]][item[1]] < 0 :
        board[item[0]][item[1]] = 0



# 틀렸던 이유
  # 빙하가 녹은걸 실시간으로 업데이트해서 그럼
  # 일괄 업데이트를 해야함