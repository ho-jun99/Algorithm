import queue
import sys
from collections import defaultdict

n = int(sys.stdin.readline())

board= []
visit = [ [ 0 for j in range(n)] for i in range(n)]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

for _ in range(n) :
  board.append(sys.stdin.readline().strip())


que = queue.Queue()
dic = defaultdict(int)

cnt = 0
for i in range(n) :
  for j in range(n) :
    # 전체 노드 중 방문하지 않은 곳이면 방문 시작

    if visit[i][j] == 0 and board[i][j] == "1":
      # 방문 하지 않은 곳이면 큐에 넣어줌
      cnt += 1
      que.put((i,j))
      visit[i][j] = cnt
      dic[cnt] +=1

    while not que.empty() :
      cur_row, cur_col = que.get()
      for dir in dirs:
        next_row = cur_row + dir[0]
        next_col = cur_col + dir[1]
        if (0<= next_row < n) and (0<= next_col < n) and visit[next_row][next_col] == 0 and board[next_row][next_col] == "1":
          visit[next_row][next_col] = cnt
          que.put((next_row,next_col))
          dic[cnt]+=1

# for i in range(n) :
#   for j in range(n) :
#     print(visit[i][j], end=" ")
#   print()

print(cnt)
for item in sorted(dic.values()) :
  print(item)