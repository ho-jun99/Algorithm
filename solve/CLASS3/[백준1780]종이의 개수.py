import sys

cnt = {-1:0,0:0,1:0}

def solve(matrix, row,col,length) :
  # print(f"{length}, {row} {col}")
  if length == 1 :
    cnt[matrix[row][col]] += 1
    return

  # 모두 같은지 확인
  checker = matrix[row][col]
  flag = True
  for i in range(length) :
    for j in range(length) :
      if checker != matrix[row+i][col+j] :
        flag = False
    if not flag :
      break

  if flag :
    # 같으면 더해주고 더이상 쪼개지 않음
    # print(f"OK {length}, {row} {col}")
    cnt[checker] += 1
    return

  # 다시 쪼개줌
  sub_length = length // 3
  for i in range(3) :
    for j in range(3) :
      solve(matrix,row+sub_length*i, col+sub_length*j, sub_length)



n = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
solve(matrix,0,0,n)
print(cnt[-1])
print(cnt[0])
print(cnt[1])
