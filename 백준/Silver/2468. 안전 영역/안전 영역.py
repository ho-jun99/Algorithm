import copy
import sys
from collections import deque

N = int(sys.stdin.readline())

board = list()
for _ in range(N) :
  line = list(map(int,sys.stdin.readline().split()))
  board.append(line)

dirs = [
  (-1,0),(0,1),(1,0),(0,-1)
  ]

maxCount = 0
for tick in range(1,101) :
  mBoard = copy.deepcopy(board)

  # 일단 안전영역 구하기
  for i in range(len(mBoard)) :
    for j in range(len(mBoard[i])) :
      if mBoard[i][j] <= tick :
        board[i][j] = -1 # 잠긴 곳임, 방문표시

  # 안전영역의 개수 세기
  cnt = 0
  for i in range(len(mBoard)) :
    for j in range(len(mBoard[i])) :
      if mBoard[i][j] == -1 :
        continue # 방문한 곳 또는 이미 잠긴 곳이면

      cnt +=1
      dq = deque()
      dq.append((i,j)) # 현재 위치 넣기
      mBoard[i][j]  # 현재 위치 방문 처리

      while len(dq) != 0 :
        cur = dq.popleft()

        for dir in dirs :
          next = (cur[0] + dir[0], cur[1] + dir[1])

          if 0 <= next[0] < N and 0 <= next[1] < N : # 범위 안이고
            if mBoard[next[0]][next[1]] != -1 : # 방문했던곳이 아니면
              # 방문처리
              mBoard[next[0]][next[1]] = -1
              dq.append(next)
  maxCount = max(maxCount,cnt)

print(maxCount)


