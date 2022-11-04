import sys

r,c = map(int,sys.stdin.readline().split())
board = list()
for i in range(r) :
  col = sys.stdin.readline().strip()
  board.append(col)

print(board)