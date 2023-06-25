import sys

def print2D(arr) :
  for i in arr :
    print(i)



N, L = map(int,sys.stdin.readline().split())
board = list()

for _ in range(N) :
  line = list(map(int,sys.stdin.readline().split()))
  board.append(line)

# print2D(board)

# flat한지 확인해야 한다.
  # Flat하다면 길이 된다.
# flat하지 않다면
  # 경사로를 놓을 수 있다.
    # 높이차이가 2 이상이라면 경사로를 놓을 수 없다.
    # 범위를 벗어나는지 확인해야한다.



# 경사로를 놓는 후보지의 공간을 찾아보자.
# 경사로가 이미 깔린 지점인지 확인하자
ground = [[False] * N for _ in range(N)]
resultA = 0
for row in range(N) :
  cur = board[row][0]
  flag = True # 해당 줄이 길이 되는지 확인해주는 flag
  for col in range(1,N) :
    if abs(cur-board[row][col]) >= 2 : # 2차이 이상이 나는 곳은 애초에 구할 수가 없다.
      flag = False
      break

    elif abs(cur-board[row][col]) == 1 : # 1차이가 나는 경우, 후보공간을 찾아볼 필요가 있을듯
      # 경사로를 놓을 수 있는 후보공간의 크기가 적합한지 판단해야함
      if cur > board[row][col] : # 2 > 1
        tr = row; tc = col
        target = cur - 1
        diff = 1
      else : # 1 < 2
        tr = row; tc = col-1
        target = cur
        diff = -1
      # 공통으로 돌리기 가능 함.
      flatSize = 0
      candidate = list()
      while flatSize < L:
        # 범위 이내이면서, 경사로가 설치되었던 곳이 아니고, 평평한 곳이라면
        if (0 <= tr < N and 0 <= tc < N) and not ground[tr][tc] and board[tr][tc] == target:
          candidate.append((tr, tc))
          flatSize += 1
          tc += diff
        else:
          break
      # 최종적으로 경사로를 놓을 수 있는 곳이라면 경사로를 놓아준다.
      # print(f"row : {row}, candidate : {candidate}")
      if flatSize == L:
        for item in candidate:
          ground[item[0]][item[1]] = True
        cur -= diff
      else:
        # 경사로를 놓을 수 없는 곳이다!
        flag = False
        break
    else : # 차이가 안나는 경우
      cur = board[row][col] # 현재 높이로 업데이트 해준다.

  if flag :
    resultA +=1
    # print("HIT row : ", row)

# 아랫길
ground = [[False] * N for _ in range(N)]
resultB = 0
for col in range(N) :
  cur = board[0][col]
  flag = True # 해당 줄이 길이 되는지 확인해주는 flag
  for row in range(1,N) :
    if abs(cur-board[row][col]) >= 2 : # 2차이 이상이 나는 곳은 애초에 구할 수가 없다.
      flag = False
      break

    elif abs(cur-board[row][col]) == 1 : # 1차이가 나는 경우, 후보공간을 찾아볼 필요가 있을듯
      # 경사로를 놓을 수 있는 후보공간의 크기가 적합한지 판단해야함
      if cur > board[row][col] : # 2 > 1
        tr = row; tc = col
        target = cur - 1
        diff = 1
      else : # 1 < 2
        tr = row-1; tc = col
        target = cur
        diff = -1
      # 공통으로 돌리기 가능 함.
      flatSize = 0
      candidate = list()
      while flatSize < L:
        # 범위 이내이면서, 경사로가 설치되었던 곳이 아니고, 평평한 곳이라면
        if (0 <= tr < N and 0 <= tc < N) and not ground[tr][tc] and board[tr][tc] == target:
          candidate.append((tr, tc))
          flatSize += 1
          tr += diff
        else:
          break
      # 최종적으로 경사로를 놓을 수 있는 곳이라면 경사로를 놓아준다.
      # print(f"row : {col}, candidate : {candidate}")
      if flatSize == L:
        for item in candidate:
          ground[item[0]][item[1]] = True
        cur -= diff
      else:
        # 경사로를 놓을 수 없는 곳이다!
        flag = False
        break
    else : # 차이가 안나는 경우
      cur = board[row][col] # 현재 높이로 업데이트 해준다.

  if flag :
    resultB +=1
    # print("HIT col : ", col)

print(resultA+resultB)