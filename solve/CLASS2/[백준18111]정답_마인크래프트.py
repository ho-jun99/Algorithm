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
  my_min = min(my_min,min(board[i]))


# print(candidate)
min_time = float('inf')
height = -1
# result = []
for i in range(my_min,my_max+1) :
  # min_time = float('inf')
  # height = -1
  target = i
  time = 0
  inventory = b
  flag = True
  time_over = False

  # 먼저 블록을 깎음(회수)
  for j in range(n) :
    for k in range(m) :
      cur = board[j][k]
      if target < cur :
        inventory += cur - target
        time += (cur-target)*2
        if time >= min_time :
          time_over = True
          break

    if time_over :
      break
  if time_over :
    continue

  # 블록을 쌓아줌
  for j in range(n) :
    for k in range(m) :
      cur = board[j][k]
      if (target > cur) :
        inventory -= target - cur
        time += (target - cur)
        if time >= min_time:
          time_over = True
          break
    if time_over :
      break
  if time_over :
    continue

  if inventory < 0 :
    flag = False

  if flag :
    # result.append((time,target))
    if min_time > time :
      min_time = time
      height = target
    elif min_time == time :
      min_time = time
      height = max(height,target)

# result.sort(key= lambda x : (x[0],-x[1]))
# print(result)
# print(f"{result[0][0]} {result[0][1]}")
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