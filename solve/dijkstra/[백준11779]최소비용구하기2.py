'''
  - 경로를 구해야 하기 때문에, 경로가 확정되면 이전에 어디서 왔는지를 distance에 함께 저장하던지, 경로 배열을 만들어서 사용해야 함
  - 최소 경로로 가는 법은 한가지 이상일 수 있음, 백준 예제는 하나만 나와서 괜히 뭐 틀린 줄 알고 찾았네..
'''

import sys
import heapq
from collections import defaultdict

n = int(sys.stdin.readline()) # 도시의 개수 = Vertex
m = int(sys.stdin.readline()) # 버스의 개수 = Edge
graph = defaultdict(list)

for _ in range(m) :
  a,b,w = map(int,sys.stdin.readline().split())
  graph[a].append((b,w))

start,end = map(int, sys.stdin.readline().split()) # 출발점 , 도착점

distance = [float('inf')] * (n+1)
route = [-1] * (n+1) # 어디로 가야할지가 적혀있음
distance[start] = 0
route[start] = start # 도착지점은 자기자신, 종료조건으로 써야할듯
heap = list()
heapq.heappush(heap,(0,start)) # 출발지점 자기자신은 0으로

while len(heap) != 0 :
  cur = heapq.heappop(heap) # ( total_weight, vertex )

  if distance[cur[1]] < cur[0] : # 이미 distance가 작다면, 결정이 끝난 것 임
    continue

  for next in graph[cur[1]] : # next : cur[1] -> ( vertex, edge_weight )
    candidate_cost = distance[cur[1]] + next[1] # 현재까지 + 이을 곳 간선
    if candidate_cost < distance[next[0]] :
      distance[next[0]] = candidate_cost # 코스트 업데이트
      route[next[0]] = cur[1] # 이전 간선 기억하기
      heapq.heappush(heap,(candidate_cost, next[0]))

cnt = 0
result = list()
def trace(node) :
  global cnt
  cnt +=1
  if route[node] == node :
    result.append(node)
    return
  trace(route[node])
  result.append(node)


trace(end)
print(distance[end]) # 도착 도시 까지 가는 데 최소 비용
print(cnt) # 도시의 개수
print(*result) # 방문하는 도시 순서