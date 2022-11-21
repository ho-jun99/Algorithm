import sys

dirs = [[-1,0],[0,1],[1,0],[0,-1]]

def solve() :
  m,n,k = map(int,sys.stdin.readline().split())
  board = [ [0 for i in range(m)] for i in range(n)]
  start_points = list()
  for i in range(k) :
    col,row = map(int,sys.stdin.readline().split())
    board[row][col] = 1
    start_points.append([row,col])
  # showBoard(board)

  cnt = 0
  q = list()
  for start_point in start_points :
    row = start_point[0]
    col = start_point[1]

    if board[row][col] == 1 :
      q.append([row, col])
      cnt+=1
    else :
      continue

    while len(q) > 0 :
      cur_row, cur_col = q.pop(0)
      if board[cur_row][cur_col] == 0 :
        continue
      else :
        for dir in dirs :
          next_row = cur_row + dir[0]
          next_col = cur_col + dir[1]
          if  0<= next_row < len(board)  and 0 <= next_col < len(board[row]) :
            if board[next_row][next_col] == 1 :
              q.append([next_row,next_col])
          else :
            continue
        board[cur_row][cur_col] = 0
        # showBoard(board)
  print(cnt)


def showBoard(board) :
  for i in range(len(board)) :
    for j in range(len(board[i])) :
      print(board[i][j], end= " ")
    print()
  print()

t = int(sys.stdin.readline())
for _ in range(t):
  solve()