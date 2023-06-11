import sys
from collections import defaultdict
from heapq import *


def print2D(arr) :
  for i in arr :
    print(*i)

# 노드의 개수
n = int(sys.stdin.readline().strip())
trees = defaultdict(list)

distance = [0] * (n+1)
visit = [-1] * (n+1)
for _ in range(n-1) :
  a,b,c = map(int,sys.stdin.readline().split())
  # 양방향 연결
  trees[a].append((b,c))
  trees[b].append((a,c))

# 다익스트라로 1번노드에서 가장 먼 정점을 구한다.
# 그정점에서 다시 다익스트라를 사용해서 가장 거리가 먼곳을 구한다
# 근데 이건 BFS써도 될거 같은데 난 다익스트라 까먹어서 다익스트라로 풀어보겠다.

def dijkstra(start) :
  global n
  h = list()
  distance = [float('inf')] * (n+1)
  distance[start] = 0 # 시작점에서 시작점으로 출발하는 경우는 0
  heappush(h,(0,start))

  while len(h) != 0 :
    cur_cost, cur_node = heappop(h) # ( cost, node )
    for next_node, next_cost in trees[cur_node] :
      updated_cost = cur_cost + next_cost
      if updated_cost < distance[next_node] :
        distance[next_node] = updated_cost
        heappush(h,(updated_cost,next_node))

  return distance

start_distance = dijkstra(1)
print(max(dijkstra(start_distance.index(max(start_distance[1:])))[1:]))


