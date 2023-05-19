'''
  - 브루트 포스를 이용해 모든경우의 수에 벽을 다 세워보자
    - 64 * 63 * 62의 벽을 세울 수 있는 경우의 수가 생긴다. 25만
    - 벽을 세우고 바이러스를 퍼트린 후 안전영역을 카운팅 해야한다.
      - BFS를 이용해 완전 탐색을 할때 시간 복잡도
  - 백트래킹느낌으로 풀어봐야겠다.
'''
import sys
from collections import deque

def print2D(arr) :
  for i in arr :
    print(i)

DIRS = [
  (-1,0), (0,1), (1,0), (0,-1)
  ]

board = list()
N,M = map(int,sys.stdin.readline().split())

for _ in range(N) :
  line = list(map(int,sys.stdin.readline().split()))
  board.append(line)

mmax = 0
def dfs(wall_cnt) :
  global board
  global mmax

  if wall_cnt == 3 :
    # 벽이 3개모두 쳐짐, 안전영역의 크기를 구하고 max값을 업데이트
    dq = deque()
    visit = [[False] * M for _ in range(N)]
    for row in range(N) :
      for col in range(M) :
        if board[row][col] == 2 :
          dq.append((row,col))
          visit[row][col] = True

    while len(dq) != 0 :
      poped = dq.popleft()
      for dir in DIRS :
        next = (poped[0] + dir[0],poped[1] + dir[1])
        if 0<= next[0] < N and 0<= next[1] < M and visit[next[0]][next[1]] == False and board[next[0]][next[1]] == 0 :
          visit[next[0]][next[1]] = True
          dq.append(next)

    cnt = 0
    for row in range(N) :
      for col in range(M) :
        if visit[row][col] == False and board[row][col] == 0 :
          cnt+=1
    mmax = max(mmax,cnt)
    return

  for row in range(N) :
    for col in range(M) :
      if board[row][col] == 0 and wall_cnt <= 2 :
        # 백트래킹 사용
        board[row][col] = 1
        dfs(wall_cnt+1)
        board[row][col] = 0

dfs(0)
print(mmax)