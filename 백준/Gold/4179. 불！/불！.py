import sys
from collections import deque

R,C = map(int, sys.stdin.readline().split())



board = list()
visit = [ [False for j in range(C) ] for i in range(R) ]
j_flag = True
f_starting = list()
j_pos = [-1,-1]


for i in range(R) :
  line = list(sys.stdin.readline().strip())
  board.append(line)
  if j_flag :
    for j in range(C) :
      if line[j] == "J" :
        j_pos[0] = i; j_pos[1] = j;
        j_flag = False

  for j in range(C) :
    if line[j] == "F" :
      f_starting.append( (i,j) )


dq = deque()
for f in f_starting :
  dq.append((f[0],f[1],"F",1))

dq.append( (j_pos[0],j_pos[1],"J",1) )

dirs = [
  (-1,0),(0,1),(1,0),(0,-1)
  ]

while len(dq) !=0 :
  cur = dq.popleft()
  if cur[2] == "J":  # 지훈이일때
    if (cur[0] == 0 or cur[0] == R - 1) or (cur[1] == 0 or cur[1] == C - 1):  # 이동전에 그곳이 탈출 구 인지 확인함
      print(cur[3])  # 여기서 탈출
      # print(board)
      exit()

  for dir in dirs :
    next = ( cur[0] + dir[0], cur[1] + dir[1], cur[2], cur[3] +1 )
    if 0<= next[0] < R and 0<= next[1] < C :
      if cur[2] == "F" : # 불일때
        if (board[next[0]][next[1]] == "." or board[next[0]][next[1]] == "J") :
          # 다음칸으로 불 이동
          dq.append(next)
          board[next[0]][next[1]] = "F"

      if cur[2] == "J" : # 지훈이일때
        if board[next[0]][next[1]] == "." : # 불이 안간 곳이면서 다음이 이동 가능할때

          if (next[0] == 0 or next[0] == R-1 ) or (next[1] == 0 or next[1] == C-1 ) : # 이동전에 그곳이 탈출 구 인지 확인함
            print(next[3]) # 여기서 탈출
            # print(board)
            exit()
          else :
            dq.append(next)
            board[next[0]][next[1]] = "J"

print("IMPOSSIBLE")

# print(board)
# print(visit)
# print("j_pos : ",j_pos)
# print("f_pos : ",f_pos)