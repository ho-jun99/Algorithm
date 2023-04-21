'''
  - 임의로 주어진 두 정점을 반드시 통과해야 한다.
  - 한번 이동했던 정점과 간선도 다시 이용할 수 있다.
  - 1번 정점부터 N번 정점으로 이동한다.
'''
import sys
from heapq import *
from collections import defaultdict

N, E = map(int, sys.stdin.readline().split())  # N : 정점의 개수 , E : 간선의 개수
graph = defaultdict(list)
for _ in range(E):
  a, b, c = map(int, sys.stdin.readline().split())
  # 무방향 그래프
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())


# 두개의 정점을 무조건 지나면서 최단 경로의 길이를 구해야 한다.
# 1 -> v1 -> v2 -> N
# 1 -> v2 -> v1 -> N
def dijkstra(start, end):
  heap = list()
  distance = [float('inf')] * (N + 1)
  distance[start] = 0
  heappush(heap, (0, start))

  while len(heap) != 0:
    cur = heappop(heap)  # (sum_weight, vertex )

    if distance[cur[1]] < cur[0]:
      continue

    for next in graph[cur[1]]:  # ( vertex, weight )
      cost = distance[cur[1]] + next[1]
      if cost < distance[next[0]]:
        distance[next[0]] = cost
        heappush(heap, (cost, next[0]))

  return distance[end]


# print(f"(v1, v2) : ({v1},{v2})")
result = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
if result == float('inf'):
  print(-1)
else:
  print(result)
