import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
# 1,1 과 N,M은 항상 0임
# 1,1 -> n,m 으로 이동해야함

visit = [[[False] * M for _ in range(N)] for i in range(2)] # 벽부수고 가는 경우랑 아닌경우 나눠야함

board = list()
for _ in range(N):
  line = list(str(sys.stdin.readline().strip()))
  line = list(map(int, line))  # 문자열을 정수로 바꾸기
  board.append(line)

# print(board)

dirs = [
  (-1, 0), (0, 1), (1, 0), (0, -1)
  ]

# 시작지점은 항상 0,0 임
# 도착지점은 항상 M,N 즉 M-1,N-1 임

# 벽을 깨는 경우와 벽을 못깨는 경우를 나눠서 생각해야함

dq = deque()
dq.append((0, 0, 1, 1))  # ( 행,열,시간,벽깰 수 있는지 여부)

while len(dq) != 0:
  cur = dq.popleft()

  if cur[0] == N - 1 and cur[1] == M - 1:
    print(cur[2])  # 최종 도착하면
    exit()

  for dir in dirs:
    next_row_col = (cur[0] + dir[0], cur[1] + dir[1])

    # 범위 체크
    if 0 <= next_row_col[0] < N and 0 <= next_row_col[1] < M:
      # 다음이 벽인지 0인지
      if board[next_row_col[0]][next_row_col[1]] == 1:  # 벽이면
        if cur[3] and visit[cur[3]][next_row_col[0]][next_row_col[1]] == False:  # 아직 벽을 깨본게 아니고 방문했던 벽이 아니라면
          dq.append((next_row_col[0], next_row_col[1], cur[2] + 1, 0))
          visit[0][next_row_col[0]][next_row_col[1]] = True

      else:
        if visit[cur[3]][next_row_col[0]][next_row_col[1]] == False:
          if next_row_col[0] == N - 1 and next_row_col[1] == M - 1:
            print(cur[2] + 1)  # 최종 도착하면
            exit()

          dq.append((next_row_col[0], next_row_col[1], cur[2] + 1, cur[3]))
          visit[cur[3]][next_row_col[0]][next_row_col[1]] = True

print(-1)
