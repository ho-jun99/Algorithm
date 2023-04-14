import sys


M, N = map(int,sys.stdin.readline().split()) # M : 행 , N : 열

board = list()
memo = [ [-1] * N for _ in range(M)]

for _ in range(M) :
  line = list(map(int,sys.stdin.readline().split()))
  board.append(line)


dirs = [
  (-1,0), (0,1), (1,0), (0,-1)
  ]

def printBoard(board) :
  for i in range(len(board)) :
    for j in range(len(board[i])) :
      print(board[i][j],end=" ")
    print()

target = (M-1, N-1)
def dfs(r,c) :
  if r == target[0] and c == target[1] :
    return 1

  if memo[r][c] >= 0 :
    return memo[r][c]

  checker = 0
  for dir in dirs :
    next = (r + dir[0], c + dir[1])
    if 0<= next[0] < M and 0<= next[1] < N : # 범위 체크

      # if memo[next[0]][next[1]] > 0 : # 이전에 방문했던 곳이면
      #   checker += memo[next[0]][next[1]]

      if board[next[0]][next[1]] < board[r][c] :
        checker += dfs(next[0],next[1]) # 다음칸으로 이동


  memo[r][c] = checker

  return checker

dfs(0,0)
# printBoard(memo)
print(memo[0][0])