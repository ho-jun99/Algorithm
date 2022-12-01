import sys


def solve(n,row,col):
  if n == 1 :
    cnt[int(board[row][col])] += 1
    return

  # n*n이 같은지 확인
  target = board[row][col]
  isSame = True
  for i in range(n) :
    for j in range(n) :
      if target != board[row+i][col+j] :
        isSame = False
        break
    if not isSame :
      break

  if isSame :
    cnt[int(board[row][col])] += 1
    return
  else :
    # 다시 나눠 줘야함
    for i in range(2) :
      for j in range(2) :
        solve(n//2, row+((n//2)*i), col+((n//2)*j))

n = int(sys.stdin.readline())
board = []
cnt = [0,0]
for _ in range(n) :
  board.append(list(sys.stdin.readline().strip().split()))

# print(board)
solve(n,0,0)
print(cnt[0])
print(cnt[1])
