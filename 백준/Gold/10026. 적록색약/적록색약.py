import sys
from collections import deque

n = int(sys.stdin.readline().strip())
board = []
visit = [[False for j in range(n)] for i in range(n)]
visitAmblyopia = [[False for j in range(n)] for i in range(n)]

for i in range(n):
  line = sys.stdin.readline().strip()
  board.append(line)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 0
cntAmblyopia = 0
## init deque
dq = deque()
dqAmblyopia = deque()


for i in range(n):
  for j in range(n) :
    if not visit[i][j] :
      dq.append((i,j))
      # 적록색약이 아닌 사람이 봤을때
      cnt +=1
      while len(dq) > 0 :
        cur = dq.popleft()
        # print("cur : " , cur)
        color = board[cur[0]][cur[1]]
        for dir in dirs :
          next = (cur[0] + dir[0], cur[1] + dir[1])
          if 0 <= next[0] < n and 0<= next[1] < n :
            if not visit[next[0]][next[1]] and board[next[0]][next[1]] == color :
              dq.append(next)
              visit[next[0]][next[1]] = True

      # 적록색약인 사람이 봤을때
      if not visitAmblyopia[i][j] :
        dqAmblyopia.append((i,j))
        cntAmblyopia+=1
        while len(dqAmblyopia) > 0:
          cur = dqAmblyopia.popleft()
          color = board[cur[0]][cur[1]]
          for dir in dirs:
            next = (cur[0] + dir[0], cur[1] + dir[1])
            if 0 <= next[0] < n and 0 <= next[1] < n:
              if not visitAmblyopia[next[0]][next[1]] :
                if color == "R" or color == "G":
                  if board[next[0]][next[1]] == "R" or board[next[0]][next[1]] == "G" :
                    dqAmblyopia.append(next)
                    visitAmblyopia[next[0]][next[1]] = True
                else :  # "B"
                  if board[next[0]][next[1]] == "B" :
                    dqAmblyopia.append(next)
                    visitAmblyopia[next[0]][next[1]] = True

print(cnt, cntAmblyopia)

