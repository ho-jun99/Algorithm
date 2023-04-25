'''
  - 오고 가야함, X까지 오는건 각각 구하고, X에서 다시 원래 지점까지 가는 방법은 X로 다익스트라 한번만 돌리면 될듯
  - total_distance를 하나 만든다
    - total_distance는 X에서 N까지의 모든 경로를 미리 구해놓는다
    - 이후 N -> X로 가는 최단거리의 값을 구해서 다익스트라를 사용해서 해당 경로에 더해준다.
'''
import sys
from collections import defaultdict
import heapq

graph = defaultdict(list)
# N명 학생, M개의 단방향 도로, X번 마을
N, M, X = map(int,sys.stdin.readline().split())
# print(f"X : {X}")

for _ in range(M) :
  # a->b, weight
  a,b,w = map(int,sys.stdin.readline().split())
  graph[a].append((b,w))


### X -> N(모든 노드)로 가는 COST를 구함 ###
total_distance = [float('inf')] * (N+1)
total_distance[X] = 0
heap = list()
heapq.heappush(heap,(0,X)) # 힙에 초기값을 넣어준다.

while len(heap) != 0 :
  cur = heapq.heappop(heap) # ( sum_weight, vertex )

  if total_distance[cur[1]] < cur[0] : # 굳이 방문할 필요가 없다.
    continue

  for next in graph[cur[1]] : # ( vertex, weight )
    cost = total_distance[cur[1]] + next[1]
    if cost < total_distance[next[0]] :
      total_distance[next[0]] = cost
      heapq.heappush(heap,(cost, next[0]))

# print(f"total_distance : {total_distance}")
### --- total_distance에 경로가 저장 됨 ###


for start in range(N+1) :
  if start == X or start == 0 : # 도착지점이기 때문에 굳이 계산할 필요가 없다.
    continue

  distance = [float('inf')] * (N+1)
  distance[start] = 0
  heap = list()
  heapq.heappush(heap,(0,start))

  while len(heap) != 0 :
    cur = heapq.heappop(heap) # ( sum_weight , vertex )

    if distance[cur[1]] < cur[0] :
      continue

    for next in graph[cur[1]] : # ( vertex, weight )
      cost = distance[cur[1]] + next[1]
      if cost < distance[next[0]] :
        distance[next[0]] = cost
        heapq.heappush(heap,(cost,next[0]))

  # print(start, distance)
  total_distance[start] += distance[X]

total_distance.sort(reverse=True)
print(total_distance[1])