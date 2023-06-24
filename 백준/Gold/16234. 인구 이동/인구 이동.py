import sys
from collections import deque


def print2D(arr):
  for i in arr:
    print(i)


dirs = [
  (-1, 0), (0, 1), (1, 0), (0, -1)
  ]

N, L, R = map(int, sys.stdin.readline().split())
board = list()
for _ in range(N):
  line = list(map(int, sys.stdin.readline().split()))
  board.append(line)

day = 0
while True:
  visit = [[False] * N for _ in range(N)]
  hit = False
  for r in range(N) :
    for c in range(N) :
      # 방문하지 않았을때 최초 시작점등록
      if not visit[r][c] :
        dq =deque()
        dq.append((r,c))
        visit[r][c] = True
        candidaties = list()
        while len(dq) != 0 :
          row,col = dq.popleft()
          for dir in dirs :
            nr = row + dir[0]
            nc = col + dir[1]
            # 국경을 열 수 있는 조건이 되는 경우
            if (0<= nr < N and 0<= nc < N) and (visit[nr][nc] == False) and L <= abs(board[row][col] - board[nr][nc])<= R :
              visit[nr][nc] = True
              dq.append((nr,nc))
              candidaties.append((nr,nc))

        if len(candidaties) != 0 :
          hit = True
          sum = 0
          candidaties.append((r,c))
          for candidate in candidaties :
            sum += board[candidate[0]][candidate[1]]
          sum //= len(candidaties)
          for candidate in candidaties :
            board[candidate[0]][candidate[1]] = sum
        else :
          # 한번도 연합을 만들지 못했으면 False로 바꿔놓는다.
            # 다른길이 뚫릴 수도 있기 때문에
          visit[r][c] = False

  if hit == False :
    break
  else :
    day +=1

print(day)


