'''
  - 동시에 미세먼지 값들을 spread시킨다
  - spread시켰다면 공기청정기의 바람에 의해 이동시킨다.
'''

import sys
from collections import deque


def print2D(arr):
  for i in arr:
    print(i)


# ROW, COL, TIME
R, C, T = map(int, sys.stdin.readline().split())
board = list()

air_conditioner = []
for row in range(R):
  line = list(map(int, sys.stdin.readline().split()))
  board.append(line)

for row in range(R) :
  if board[row][0] == -1 :
    air_conditioner.append((row,0))

# print(air_conditioner)
dirs = [
  (-1,0), (0,1), (1,0), (0,-1)
  ]

reverse_dir = [
  (0,1), (-1,0), (0,-1),(1,0)
  ]
right_dir = [
  (0,1), (1,0), (0,-1), (-1,0)
  ]

def spread():
  global board, R, C, T
  dq = deque()

  # 미세먼지가 있는 시작점의 위치를 모두 파악한다.
  for row in range(R) :
    for col in range(C) :
      if board[row][col] > 0 : # 0보다 큰 곳이라면
        dq.append((row,col,board[row][col]//5)) # row,col, 퍼트릴 미세먼지

  # 미세먼지를 퍼트린다. 단 동시 시간대에 퍼트려야 한다.
  candidate= list()
  while len(dq) !=0 :
    poped = dq.popleft() # (row, col, 퍼트릴 미세먼지)

    spread_count = 0
    for dir in dirs :
      next = (poped[0] + dir[0], poped[1] + dir[1])
      if 0<= next[0] < R and 0<= next[1] < C and 0 <= board[next[0]][next[1]] :
        candidate.append((next[0],next[1],poped[2])) # 퍼트려진 미세먼지 후보군에 저장
        spread_count +=1
    candidate.append((poped[0],poped[1], poped[2]*spread_count*-1)) # 현재 위치에서 뺴야할 것

  # 퍼트린 미세먼지 기반으로 board를 업데이트 한다.
  for item in candidate : # (row,col,updating_num)
    board[item[0]][item[1]] += item[2]


def run_air() :
  global board, R, C, T, air_conditioner

  for i in range(2) :
    before = (air_conditioner[i][0],0,0)
    if i == 0 :
      mdir = reverse_dir
    else :
      mdir = right_dir

    for dir in mdir :
      while True :
        cur = (before[0] + dir[0], before[1] + dir[1])
        if 0<= cur[0] < R and 0<= cur[1] < C :
          if board[cur[0]][cur[1]] == -1 : # 공기청정기가 존재하는 위치일때
            break
          temp = (cur[0], cur[1],board[ cur[0] ][ cur[1] ] )
          board[cur[0]][cur[1]] = before[2]
          before = temp
        else :
          break


for t in range(T) :
  spread()
  run_air()

# 미세먼지의 갯수를 센다
result = 0
for row in range(R) :
  for col in range(C) :
    if board[row][col] > 0 :
      result += board[row][col]

print(result)
