import sys
from heapq import *
from collections import defaultdict

# N 도시의 수, M 도로의 수, K 면접장의 수
N, M, K = map(int, sys.stdin.readline().split())

graph =defaultdict(list)
for _ in range(M) :
  u,v,c = map(int,sys.stdin.readline().split())
  graph[v].append((u,c)) # 단방향을 거꾸로 연결시킨다.
targets = list(map(int,sys.stdin.readline().split()))

# - 문제 접근 방법-
# 그래프를 거꾸로 연결 시킨다. a -> b 였다면, b -> c와 같은 형태로
# 거꾸로 연결시킨 그래프을 통해서, 시작 정점을 target으로 하여금 하여 가장 먼 곳을 찾아본다.

def dijkstra() :
  distance = [float('inf')] * (N + 1)
  heap = list()

  for target in targets :
    distance[target] = 0
    heappush(heap, (0, target))

  while len(heap) != 0 :
    cur = heappop(heap) # ( sum_weight , vertex )

    if distance[cur[1]] < cur[0] :
      continue

    for next in graph[cur[1]] : # ( vertex, weight )
      cost = distance[cur[1]] + next[1]
      if cost < distance[next[0]] :
        distance[next[0]] = cost
        heappush(heap,(cost, next[0]))
  return distance

result = dijkstra()
i = max(result[1:])
print(result.index(i))
print(i)