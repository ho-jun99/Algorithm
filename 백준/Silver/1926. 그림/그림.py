import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split()) # n 세로크기 , m 가로크기

board = list()
visit = [[ False for j in range(m) ] for i in range(n)]
for i in range(n) :
  row = list(map(int,sys.stdin.readline().split()))
  board.append(row)

dirs = [
  (-1,0),(0,1),(1,0),(0,-1)
  ]

max_size = 0
cnt = 0

for row in range(len(visit)) :
  for col in range(len(visit[row])) :
    if visit[row][col] == False and board[row][col] == 1:
      dq = deque()
      start = (row,col)
      local_size = 1
      visit[row][col] = True
      dq.append(start)
      cnt +=1

      while len(dq) != 0 :
        cur = dq.popleft()
        for dir in dirs :
          next = (cur[0]+dir[0], cur[1]+dir[1])
          if 0 <= next[0] < n and 0 <= next[1] < m:
            if visit[next[0]][next[1]] == False and board[next[0]][next[1]] == 1:
              dq.append(next)
              local_size +=1
              visit[next[0]][next[1]] = True
      max_size = max(max_size,local_size)

# print(board)
# print(visit)

# print("cnt : ", cnt)
# print("size : ", max_size)

print(cnt)
print(max_size)
