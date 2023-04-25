import sys
from collections import deque

# N : 도시의 수, M : 도로의 수, K : 포장할 도로의 수
N, M, K = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]


for _ in range(M):
  a, b, w = map(int, sys.stdin.readline().split())
  # 양방향 도로 , False = 미방문
  graph[a].append((b, w))
  graph[b].append((a, w))

# BFS로 목표지점(N)까지 가는 모든 경로와 그 경로의 가중치를 구하고
# 가장 큰 가중치를 K번씩 하나씩 0으로 바꾸었을때 min값을 찾아본다.
# 근데 다익스트라로도 모든 경로를 구할 수 있지 않은가?
dq = deque()
dq.append((1, [0]))  # ( start, [ 이전에 방문한 곳의 weight ]
visit = set([(1, 0)])  # visit 체크
results = list()

while len(dq) != 0:
  cur = dq.popleft()

  for next in graph[cur[0]]:  # (b,w)
    if (next[0], cur[1][-1] + next[1]) in visit:  # 방문했던 곳이면 넘어감
      continue
    if next[0] == N:  # 목표지점이면
      results.append(cur[1] + [next[1]])
    else:
      # 방문체크
      visit.add((next[0], cur[1][-1] + next[1]))
      dq.append((next[0], cur[1] + [next[1]]))  # 큐에 넣기

mmin = float('inf')
for result in results:
  for i in range(K):
    result[result.index(max(result))] = 0
  mmin = min(mmin, sum(result))
print(mmin)
