import sys

board = list()
N,M = map(int,sys.stdin.readline().split())

for i in range(N) :
  l = sys.stdin.readline().strip()
  board.append(l)
result = [ [0 for i in range(M)] for j in range(N)]
for i in range(N) :
  for j in range(M) :
    result[i][M-1-j] = board[i][j]

for i in range(N) :
  for j in range(M) :
    print(result[i][j],end="")
  print()