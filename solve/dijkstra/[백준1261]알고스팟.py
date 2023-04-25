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
from collections import deque


M, N = map(int, sys.stdin.readline().split())  # M: col, N : row

board = list()

dirs = [
  (-1, 0), (0, 1), (1, 0), (0, -1)
  ]

for _ in range(N):
  line = list(map(int, sys.stdin.readline().strip()))
  board.append(line)

###### ---  0-1 BFS 풀이 --- ######
# 탐색기준은 벽을 적게 부수는 순위

distance = [ [0] * M for _ in range(N)]
visit = [ [False] * M for _ in range(N)]
visit[0][0] = True

def print2D(arr) :
  for i in range(len(arr)) :
    for j in range(len(arr[i])) :
      print(arr[i][j],end =" ")
    print()
  print()

deque = deque()
deque.append((0,0))

while len(deque) != 0 :
  cur = deque.popleft() # ( row, col )
  # print2D(distance)

  if cur[0] == N - 1 and cur[1] == M - 1:
    print(distance[N - 1][M - 1])
    exit()

  for dir in dirs :
    next = (cur[0] + dir[0], cur[1] + dir[1])
    if 0<= next[0] < N and 0<= next[1] < M and visit[next[0]][next[1]] == False:
      if board[next[0]][next[1]] == 0 :
        deque.appendleft(next)
        visit[next[0]][next[1]] = True
      else :
        deque.append(next)
        visit[next[0]][next[1]] = True
      distance[next[0]][next[1]] += distance[cur[0]][cur[1]] + board[next[0]][next[1]]
###### ---  ------------ --- ######


# ###### ---  다익스트라 풀이 --- ######
# distance = [[float('inf')] * M for _ in range(N)]
# distance[0][0] = 0  # 출발지점
# heap = list()
# heapq.heappush(heap, (0, 0, 0))  # 출발시 가중치, 출발 좌표
# target = (N,M)
#
# while len(heap) != 0:
#   cur = heapq.heappop(heap) # ( weight, row, col )
#
#   if distance[cur[1]][cur[2]] < cur[0] :
#     continue
#
#   for dir in dirs :
#     next = (cur[1] + dir[0], cur[2] + dir[1])
#
#     if 0<= next[0] < N and 0<= next[1] < M : # 범위 안이라면
#       cost = distance[cur[1]][cur[2]] + board[next[0]][next[1]]
#
#       if cost < distance[next[0]][next[1]] :
#         distance[next[0]][next[1]] = cost
#         heapq.heappush(heap,(cost,next[0],next[1]))
#
# print(distance[N-1][M-1])
# ###### ---  ------------ --- ######