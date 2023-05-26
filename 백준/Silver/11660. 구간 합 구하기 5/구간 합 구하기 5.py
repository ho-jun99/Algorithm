import sys

def print2D(arr) :
  for i in arr :
    print(*i)
  print()

N,M = map(int,sys.stdin.readline().split())

board = list()
for _ in range(N) :
  line = list(map(int,sys.stdin.readline().split()))
  board.append(line)

targets = list()
for _ in range(M) :
  target = list(map(int,sys.stdin.readline().split()))
  targets.append(target)

# board를 누적합 배열로 만들어 놓고, 문제 풀이시 한번에 solve가능하도록 하자
for row in range(N) :
  for col in range(1,N) :
    board[row][col] += board[row][col-1]

# print2D(board)


for target in targets :
  r1,c1,r2,c2 = target
  r1 -= 1; c1 -=1; r2 -=1; c2 -=1; # 인덱싱 보정
  result = 0

  for r in range(r1,r2+1) :
    result += board[r][c2]
    if c1 == 0 :
      minus = 0
    else :
      result -= board[r][c1-1]

  print(result)