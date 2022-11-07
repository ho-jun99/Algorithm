# 10
# 1  2  3  4
# 5  6  7  8
# 9 10 11 12

import sys
n,m,b = map(int,sys.stdin.readline().split())

board = []

for i in range(n) :
  board.append(list(map(int,sys.stdin.readline().rstrip().split())))
# print(board)

# 목표는 땅의 높이를 일정하게 맞추는 것
# 블록을 제거하여 인벤토리에 넣는 경우 time + 2
# 블록을 꺼내 쌓는 경우 time + 1

# 출력은 걸리는 시간 / 땅의 높이
# n,m,b

candidate = list()
my_max = -1
my_min = float('inf')
for i in range(n) :
  my_max = max(my_max,max(board[i]))


# print(candidate)
min_time = float('inf')
height = -1
# result = []
for i in range(0,my_max+1) :
  get = 0 # 얻은 블록
  use = 0 # 사용한 블럭
  time = 0
  for j in range(n) :
    for k in range(m) :
      cur = board[j][k]
      if cur < i : # i만큼 채우기 위해서 블록을 사용해야함
        use += i - cur
      else : # i만큼 깎고 블록을 저장함
        get += cur - i
  inventory = get + b
  if inventory < use :
    continue
  # print(f"get : {get} use : {use} i {i}")
  time += 2*get
  time += use

  if time <= min_time :
    min_time = time
    height = i # 어차피 밑에서부터 위로 올라가면서 결국 최대 높이에서 끝나게 됨


print(f"{min_time} {height}")

# 3 4 0
# 64 64 64 64
# 64 64 64 64
# 64 64 64 63

# 3 4 99
# 0 0 0 0
# 0 0 0 0
# 0 0 0 1

# 1 3 68
# 0 0 1

# 3 4 11
# 29 51 54 44
# 22 44 32 62
# 25 38 16 2

# 1 1 0
# 0

## //768 128
# 2 2 0
# 256 256
# 0 0

# 1 3 68
# 0 0 1