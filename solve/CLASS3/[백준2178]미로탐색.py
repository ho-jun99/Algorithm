import queue
import sys

n,m = map(int,sys.stdin.readline().strip().split())


# (0,0) -> (n-1,m-1) 도착 (인덱스번호)
board = []
for i in range(n) :
  board.append(sys.stdin.readline().strip())

# bfs를 이용한 최단경로 풀이를 진행해야함
que = queue.Queue()
visit = [[False for i in range(m)] for j in range(n)]
cnt = [[0 for i in range(m)] for j in range(n)]


dirs = [(-1,0),(0,1),(1,0),(0,-1)]

que.put((0,0))
cnt[0][0] = 1

while not que.empty() :
  cur_row,cur_col = que.get()
  if cur_row == n-1 and cur_col== m-1 :
    break
  for dir in dirs :
    next_row = cur_row + dir[0]
    next_col = cur_col + dir[1]
    if 0<= next_row < n and 0<= next_col < m :
      if int(board[next_row][next_col]) == 1 and visit[next_row][next_col] == False:
        # 방문해야함
        visit[next_row][next_col] = True
        que.put((next_row,next_col))
        cnt[next_row][next_col] = cnt[cur_row][cur_col] + 1


print(cnt[n-1][m-1])
