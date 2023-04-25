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
# 그래프를 거꾸로 연결 시킨다. a -> b 였다면, b -> a와 같은 형태로
# 다익스트라를 한번만 돌리고, 이때 힙에 모든 면접장을 다 넣어준다
  # 한 정점으로부터 모든 정점까지의 경로를 구하는 것이 아니다.
  # 면접장으로부터 가장 가까운 노드만 구하면 되기 때문에, 힙에 면접장을 모두 넣어도 된다.


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
# #--------- 시간초과 풀이 ----------#
# # N-> K 까지 이동해야함
# def dijkstra(start) :
#   distance = [float('inf')] * (N+1)
#   distance[start] = 0
#   heap = list()
#   heappush(heap,(0,start))
#
#   while len(heap) != 0 :
#     cur = heappop(heap) # ( sum_weight, vertex )
#
#     if distance[cur[1]] < cur[0] :
#       continue
#
#     for next in graph[cur[1]] : # ( vertex, weight )
#       cost = distance[cur[1]] + next[1]
#       if cost < distance[next[0]] :
#         distance[next[0]] = cost
#         heappush(heap,(cost, next[0]))
#
#   # 여기서 최단거리를 뽑아야함
#   # 타겟중에서 최단거리를 뽑아야함
#   mmin = float('inf')
#   for target in targets :
#     mmin = min(distance[target], mmin)
#
#
#   return (start, mmin)
#
# mmax = (-1, -1)
# for i in range(1,N+1) :
#   result = dijkstra(i)
#   # print(result)
#   mmax = max( mmax, result, key=lambda x: (x[1], -x[0]))
#
# print(mmax[0])
# print(mmax[1])