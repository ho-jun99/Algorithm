'''
  1. 다익스트라는 시작정점으로부터 모든 정점까지의 최단거리를 구할 수 있다
  2. 간선(Edge)의 값이 0 이상의 양수일때 정상 작동한다.
  - 최단 거리 테이블 초기화( 시작 노드 0, 나머지 inf )
  - https://www.acmicpc.net/board/view/82405 그래프 관련
'''
import heapq
import sys
from collections import defaultdict

V,E = map(int, sys.stdin.readline().split())
start_vertex = int(sys.stdin.readline())
graph = defaultdict(list) # defaultdict 때문에 틀리는 문제 발생

distance = [float("inf")] * (V+1) # 거리 업데이트 배열, 방문처리를 여기서 -1로 해줄 수 있음 ( 음수 가중치가 없기때문에)
distance[start_vertex] = 0
heap = list()
heapq.heappush(heap,(0, start_vertex)) # 힙에 시작노드 넣어주기

#  u -> v , weight
for _ in range(E) :
  # 그래프 구성하기
  u,v,w = map(int,sys.stdin.readline().split())
  graph[u].append((v,w))

while len(heap) != 0 :
  cur = heapq.heappop(heap) # ( weight, vertex)
  # print(distance, cur)

  if distance[cur[1]] < cur[0] :
    continue # 큐에서 뽑아낸 값과 갱신된 거리 비교, 방문처리가 된 곳임.

  for neighbor in graph[cur[1]] :
    cost = distance[cur[1]] + neighbor[1]
    # print(f"cost : {cost}")
    if cost < distance[neighbor[0]] :
      distance[neighbor[0]] = cost
      heapq.heappush(heap, (cost , neighbor[0]))


for i in range(1,V+1) :
  if distance[i] == float('inf'):
    print("INF")
  else :
    print(distance[i])