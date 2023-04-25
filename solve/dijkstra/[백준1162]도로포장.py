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

# ### ------ 시간초과 ------ ###
# # BFS로 목표지점(N)까지 가는 모든 경로와 그 경로의 가중치를 구하고
# # 가장 큰 가중치를 K번씩 하나씩 0으로 바꾸었을때 min값을 찾아본다.
#   # 근데 다익스트라로도 모든 경로를 구할 수 있지 않은가?
# dq = deque()
# dq.append((1, [0])) #( start, [ 이전에 방문한 곳의 weight ]
# visit = [[False] * (N+1) for _ in range(N+1)]
# visit[1][1] = True
# results = list()
#
#
# while len(dq) != 0 :
#   cur = dq.popleft()
#
#   for next in graph[cur[0]] : # (b,w)
#     if visit[cur[0]][next[0]] : # 방문했던 곳이면 넘어감
#       continue
#
#     copyed = cur[1] + [next[1]]
#     # print(copyed)
#     # copyed = copy.deepcopy(cur[1])
#     # copyed.append(next[1])
#     q_next = (next[0], copyed)
#     if q_next[0] == N : # 목표지점이면
#       results.append(q_next[1])
#     else :
#       # 방문체크
#       visit[cur[0]][next[0]] = True
#       visit[next[0]][cur[0]] = True
#       dq.append(q_next)# 큐에 넣기
#
# # print(results)
#
# mmin = float('inf')
# for result in results :
#   for i in range(K) :
#     result[result.index(max(result))] = 0
#   mmin = min(mmin,sum(result))
# print(mmin)


