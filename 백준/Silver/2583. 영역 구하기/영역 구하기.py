import sys
from collections import deque


M,N,K = map(int, sys.stdin.readline().split())
# M 행 , N 열

board = [ [False] * N for i in range(M)]

def printBoard() :
  for i in range(M) :
    print(board[i])

dirs = [
  (-1,0),(0,1),(1,0),(0,-1)
  ]

for _ in range(K) :
  x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      board[i][j] = True

# printBoard()

cnt = 0
sizes = list()

for row in range(M) :
  for col in range(N) :
    size = 1
    if board[row][col] == False :
      cnt +=1
      # bfs로 세는거 시작해야함
      dq = deque()
      dq.append( (row,col))
      board[row][col] = True # 방문처리
      while len(dq) != 0 :
        cur = dq.popleft()

        for dir in dirs :
          next = ( cur[0] + dir[0], cur[1] + dir[1])

          # 범위 안에 드는지 확인
          if 0<= next[0] < M and 0<= next[1] < N :
            # 방문했는지 확인하기
            if board[next[0]][next[1]] == False :
              # 방문 및 넓이 카운트 하기
              board[next[0]][next[1]] = True
              size +=1
              dq.append(next)
      sizes.append(size)

print(cnt)
sizes.sort()
for _ in range(len(sizes)) :
  print(sizes[_],end=" ")
