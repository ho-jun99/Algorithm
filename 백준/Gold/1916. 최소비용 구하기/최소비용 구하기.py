import sys
import heapq
from collections import defaultdict

N = int(sys.stdin.readline()) # 도시의 개수
M = int(sys.stdin.readline()) # 버스의 개수

graph = defaultdict(list)

for _ in range(M) :
  a,b,w = map(int,sys.stdin.readline().split())
  graph[a].append((b,w))

start,end = map(int,sys.stdin.readline().split())

distance = [float("inf")] * (N+1)
distance[start] = 0 # 시작 지점 설정해주기
heap = list()
heapq.heappush( heap,(0,start) )

while len(heap) != 0 :
  cur = heapq.heappop(heap) # ( total_weight , vertex )

  if distance[cur[1]] < cur[0] : # 이미 방문이 완료 된 노드임
    continue

  for next in graph[cur[1]] : # ( vertex, weight )
    cost = distance[cur[1]] + next[1]

    if cost < distance[next[0]] :
      distance[next[0]] = cost # distance 업데이트
      heapq.heappush( heap,(cost, next[0]) )

print(distance[end])