import sys


def solve():
  row,col = map(int,sys.stdin.readline().strip().split())
  castle = []

  for i in range(row):
    castle.append(sys.stdin.readline().strip())

  plus_row = 0
  for i in range(row):
    row_guard = False
    for j in range(col):
      if castle[i][j] == 'X':
        row_guard = True

    if not row_guard:
      # 해당 행에는 경비원이 없음
      plus_row += 1

  plus_col = 0
  for i in range(col):
    col_guard = False
    for j in range(row):
      if castle[j][i] == 'X':
        col_guard = True
    if not col_guard :
      plus_col +=1

  print(max(plus_col,plus_row))


if __name__ == '__main__':
  solve()