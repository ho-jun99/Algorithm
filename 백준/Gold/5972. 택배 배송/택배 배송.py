import sys
import heapq
from collections import defaultdict

def print2D(arrs) :
  print("---")
  for arr in arrs :
    print(arr)

N,M = map(int,sys.stdin.readline().split())
graph = defaultdict(list)

for i in range(M) :
  # 들어오는 값에 1을 빼줘서 배열을 보정함
  start,end,cost = map(int,sys.stdin.readline().split())
  start -=1
  end -=1

  # 양방향 연결
  graph[start].append((end,cost))
  graph[end].append((start,cost))

# 무한대 처리를 해놓는다.
distance = [float('inf') for i in range(N)]
# 시작위치 ( 0 ) 을 설정 해 놓는다.
distance[0] = 0
heap = list()
heapq.heappush(heap,(0,0)) # cost, 시작위치

while len(heap) != 0 :
  curCost, start = heapq.heappop(heap)

  if distance[start] < curCost : # 현재 계산된 거리가, 뽑아낸 거리보다 짧으면 굳이 갈 필요가 없다.
    continue

  for next in graph[start] :
    end = next[0]
    nextCost = next[1]
    candidateCost = curCost + nextCost
    if candidateCost < distance[end] :
      # 기존꺼보다, 새롭게 뚫린길이 더 짧은 길일때 새롭게 업데이트 하고
      distance[end] = candidateCost
      # heap에다가 넣어버린다.
      heapq.heappush(heap,(candidateCost,end))

# print(distance)
print(distance[N-1])