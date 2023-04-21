'''
  - (1,1) -> (M,N) 으로 이동해야함
  - 무조건 아래랑 오른쪽으로 가는것만 사용해야 하는거 아님?
    - 벽을 최소개로 부수는거지, 최단으로 이동하는 문제는 아닌거 같다
  - 이문제는 0,1(BFS) 가중치 문제로 풀어볼 수 있겠다.
  - 벽을 최소한으로 부수는거이기 때문에 벽을 부수는데 가중치를 1로 두자
  - 0-1bfs와 다익스트라로 풀 수 있을것 같다.
'''

import sys
import heapq

M, N = map(int, sys.stdin.readline().split())  # M: col, N : row

board = list()

dirs = [
  (-1, 0), (0, 1), (1, 0), (0, -1)
  ]

for _ in range(N):
  line = list(map(int, sys.stdin.readline().strip()))
  board.append(line)

distance = [[float('inf')] * M for _ in range(N)]
distance[0][0] = 0  # 출발지점
heap = list()
heapq.heappush(heap, (0, 0, 0))  # 출발시 가중치, 출발 좌표
target = (N,M)

while len(heap) != 0:
  cur = heapq.heappop(heap) # ( weight, row, col )

  if distance[cur[1]][cur[2]] < cur[0] :
    continue

  for dir in dirs :
    next = (cur[1] + dir[0], cur[2] + dir[1])

    if 0<= next[0] < N and 0<= next[1] < M : # 범위 안이라면
      cost = distance[cur[1]][cur[2]] + board[next[0]][next[1]]

      if cost < distance[next[0]][next[1]] :
        distance[next[0]][next[1]] = cost
        heapq.heappush(heap,(cost,next[0],next[1]))

print(distance[N-1][M-1])
