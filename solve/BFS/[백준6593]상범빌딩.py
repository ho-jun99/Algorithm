import sys
from collections import deque

dirs = [
  (-1, 0, 0),  # 아래
  (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1),  # 상하좌우
  (1, 0, 0)  # 위로
  ]


def solve(L, R, C):
  board = list()
  start_point = [-1, -1, -1]
  flag = True

  ### BOARD 구성 ###
  for l in range(L):
    temp = list()
    for r in range(R + 1):
      inputStr = str(sys.stdin.readline().strip())
      line = list(inputStr)
      if len(line) == 0:
        continue
      if flag and 'S' in inputStr:
        c = inputStr.find('S')
        if c != -1:
          start_point[0] = l
          start_point[1] = r
          start_point[2] = c
          flag = False

      temp.append(line)
    board.append(temp)

  # print(board)
  # print("start_point : ", start_point)
  #####################

  dq = deque()
  dq.append((start_point[0], start_point[1], start_point[2], 0))  # 초기 시작값
  board[start_point[0]][start_point[1]][start_point[2]] = "#"  # # 방문 처리

  while len(dq) != 0:
    cur = dq.popleft()  # 꺼내기

    for dir in dirs:
      next = (cur[0] + dir[0], cur[1] + dir[1], cur[2] + dir[2], cur[3] + 1)

      if 0 <= next[0] < L and 0 <= next[1] < R and 0 <= next[2] < C:  # 범위 안인지 확인
        if board[next[0]][next[1]][next[2]] == ".":  # 갈 수 있는 곳인지 확인
          dq.append(next)  # 추가해주기
          board[next[0]][next[1]][next[2]] = "#"  # 방문처리

        elif board[next[0]][next[1]][next[2]] == "E":  # 목표 지점이면
          return next[3]  # 끝내기
  return -1


while True:
  L, R, C = map(int, sys.stdin.readline().split())
  # L 층 수
  # R 행, C 열
  if L == 0 and R == 0 and C == 0:
    break
  result = solve(L, R, C)
  if result == -1:
    print("Trapped!")
  else:
    print(f"Escaped in {result} minute(s).")
