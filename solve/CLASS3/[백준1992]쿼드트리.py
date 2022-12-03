import sys



def solve(row,col,n) :
  if n == 1 : return print(board[row][col],end="")


  target = board[row][col]
  isSame = True
  # 전체가 같은지 탐색
  for i in range(row,row+n) :
    for j in range(col,col+n) :
      if board[i][j] != target :
        isSame = False
    if not isSame :
      break
  if isSame :
    return print(target,end="")

  # 4블럭 탐색 후 틀린 지점 재귀 호출
  print("(", end="")
  half = n // 2
  for i in range(2) :
    for j in range(2) :
      solve(row+(i*half),col+(j*half),half)
  print(")",end="")

n = int(sys.stdin.readline())
board = [ sys.stdin.readline().strip() for i in range(n) ]
solve(0,0,n)

# 8
# 00000000
# 00000000
# 00001111
# 00001111
# 00011111
# 00111111
# 00111111
# 00111111