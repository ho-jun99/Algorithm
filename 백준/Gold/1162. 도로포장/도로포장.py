import sys
from collections import defaultdict
from heapq import *

# N : 도시의 수, M : 도로의 수, K : 포장할 도로의 수
N, M, K = map(int,sys.stdin.readline().split())
graph = defaultdict(list)


for _ in range(M) :
  a,b,w = map(int,sys.stdin.readline().split())
  # 무방향 도로
  graph[a].append((b,w))
  graph[b].append((a,w))

# 길을 까는것과 안까는 걸로 계속 나눠가는 형식으로 해보자
distance = [[float('inf')] * (N+1) for _ in range(K+1)] # 도로를 깔 수 있는 만큼
for i in range(K+1) :
  distance[i][1] = 0 # 초기 설정

heap = list()
heappush(heap, (0, 1, K)) # ( sum_weight, vertex, 현재 포장가능한 도로의 수 )

while len(heap) != 0 :
  cur = heappop(heap) # # ( sum_weight, vertex, 현재 포장가능한 도로의 수 )

  if distance[cur[2]][cur[1]] < cur[0] :
    continue

  for next in graph[cur[1]] : # ( vertex, weight )
    cost = distance[cur[2]][cur[1]] + next[1] # 도로를 깔지 않을때
    if cost < distance[cur[2]][next[0]] :
      distance[cur[2]][next[0]] = cost
      heappush(heap,(cost,next[0],cur[2]))

    if cur[2] > 0 : # 도로를 깔 수 있을 때
      cost = distance[cur[2]][cur[1]] + 0 # 0을 더해서 다음경로까지가 완성 됨
      if cost < distance[cur[2]-1][next[0]] :
        distance[cur[2]-1][next[0]] = cost
        heappush(heap,(cost,next[0],cur[2]-1))

mmin = float('inf')
for i in range(K+1) :
  mmin = min(mmin,distance[i][N])
print(mmin)
