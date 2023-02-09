import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
  line = list(map(int, sys.stdin.readline().split()))
  board.append(line)

# print(board)

blocks = [

    # ㅡ
    [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (0, 2), (0, 3)],

    # ㅁ
    [(0, 1), (1, 0), (1, 1)],

    # L
    [(1, 0), (2, 0), (2, 1)],
    [(0, 1), (0, 2), (1, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (-1, 2)],

    # reverse(L)
    [(0, 1), (-1, 1), (-2, 1)],
    [(1, 0), (1, 1), (1, 2)],
    [(0, 1), (1, 0), (2, 0)],
    [(0, 1), (0, 2), (1, 2)],

    # ㅗ
    [(0, 1), (0, 2), (-1, 1)],
    [(1, 0), (2, 0), (1, 1)],
    [(0, 1), (0, 2), (1, 1)],
    [(0, 1), (1, 1), (-1, 1)],

    # ㄴㄱ
    [(1, 0), (1, 1), (2, 1)],
    [(0, 1), (-1, 1), (-1, 2)],

    # Reverse(ㄴㄱ)
    [(-1, 0), (-1, 1), (-2, 1)],
    [(0, 1), (1, 1), (1, 2)],
  ]

# 보드에 대입해서 최대값을 구하기
mMax = 0
sum = 0
for i in range(n):
  for j in range(m):
    cur = (i,j)

    for block in blocks:
      mMax = max(mMax,sum)
      sum = board[cur[0]][cur[1]]
      isBoardIn = True
      for point in block:
        next = (cur[0] + point[0], cur[1] + point[1])
        if 0<= next[0] < n and 0 <= next[1] < m :
          sum += board[next[0]][next[1]]
        else :
          isBoardIn = False
          sum = -1
          break

print(mMax)