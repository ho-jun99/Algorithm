import sys
from collections import deque

dirs = [
  (-1,0) , (-1,1) ,(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)
  ]

def solve(w,h) :
  board = list()
  for _ in range(h) :
    line = list(map(int,sys.stdin.readline().strip().split()))
    board.append(line)

  cnt = 0
  for r in range(h) :
    for c in range(w) :
      if board[r][c] == 0 :
        continue
      else :
        cnt +=1
        stk = deque()
        stk.append((r,c))
        board[r][c] = 0 # 초기상태 방문표시

        while len(stk) != 0 :
          cur = stk.pop() # STACK을 사용하는 DFS 풀이
          for dir in dirs :
            next = (cur[0]+dir[0], cur[1]+dir[1])

            if 0<= next[0] < h and 0<= next[1] < w : # 보드 안에 있을 때
              if board[next[0]][next[1]] == 1 : # 방문이 가능한 곳이면
                stk.append(next)
                board[next[0]][next[1]] = 0 # 방문처리

  print(cnt)


while True :
  w,h = map(int,sys.stdin.readline().split())
  if w == 0 and h == 0 :
    break
  else :
    solve(w,h)