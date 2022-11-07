import copy
import sys

r,c = map(int,sys.stdin.readline().split())
board = list()
for i in range(r) :
  col = str(sys.stdin.readline().strip())
  board.append(col)
# print(board)
start_w = "WBWBWBWB"
start_b = "BWBWBWBW"

result = []
for i in range(0,len(board)-7) :
  for j in range(0,len(board[i])-7) :
    cnt = 0

    # 시작이 W인 경우
    is_start_w = True
    for k in range(8) :
      for l in range(8) :
        if is_start_w :
          if board[i+k][j+l] != start_w[l] :
            cnt +=1
        else :
          if board[i+k][j+l] != start_b[l] :
            cnt +=1
      is_start_w = False if is_start_w == True else True
    result.append(cnt)

    # 시작이 B인 경우
    cnt = 0
    is_start_w = False
    for k in range(8):
      for l in range(8):
        if is_start_w:
          if board[i + k][j + l] != start_w[l]:
            cnt += 1
        else:
          if board[i + k][j + l] != start_b[l]:
            cnt += 1
      is_start_w = False if is_start_w == True else True
    result.append(cnt)
    cnt = 0

print(result)
print(min(result))