'''
  - 한 정점에서 모든정점까지의 최단거리를 구하자. ( X )
    - 다익스트라 알고리
  - 아니다 문제를 잘못 봤다. 플로이드 와샬로 모든정점에서 모든정점까지의 최단거리를 구해야 한다.

'''
import sys

def print2D(arr) :
  for i in arr :
    print(*i)

# n : 지역의 개수
# m : 수색범위
# r : 길의 개수
n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
graph = [[float('inf')] * (n+1) for _ in range(n+1)]

for _ in range(r):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a][b] = min(graph[a][b], c)
  graph[b][a] = min(graph[b][a], c)

# 대각행렬(자기 자신)은 0으로 초기화 한다.
for i in range(n+1) :
  graph[i][i] = 0

for pivot in range(1,n+1) :
  for start in range(1,n+1) :
    for end in range(1,n+1) :
      cost = graph[start][pivot] + graph[pivot][end] # 피벗을 거쳐가는 것과 비교하기 위해서
      if cost < graph[start][end] :
        graph[start][end] = cost

# print2D(graph)

result = 0
for start in range(1,n+1) :
  sum = 0
  for end in range(1,n+1) :
    if graph[start][end] <= m : # 수색범위 이내이면
     sum  += items[end-1] # 범위 맞춰줘야함
  result = max(result,sum)

print(result)

