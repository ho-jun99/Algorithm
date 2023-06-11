import sys
from collections import defaultdict
from collections import deque

# 정점의 개수
V = int(sys.stdin.readline().strip())
trees = defaultdict(list)

for _ in range(V) :
  line = list(map(int,sys.stdin.readline().split()))

  node = line[0]
  loop_idx = 1
  while loop_idx < len(line)-1 :
    trees[node].append((line[loop_idx], line[loop_idx+1]))
    loop_idx+=2

# 현재 트리는 양방향 연결인 점에 주의
# 무작위 한 정점에서 가장 거리가 먼 곳을 찾는다.
  # 이번엔 BFS를 이용해서 찾아보자.
  # 트리는 애초에 사이클이 없다.

# 시작노드로부터 멀리 떨어진 노드를 찾는다.
def bfs(start) :
  global trees, V

  dq = deque()
  visit = [-1] * (V+1)
  visit[start] = 0
  dq.append((start,0))

  while len(dq) != 0 :
    cur_node, cur_weight = dq.popleft()
    for next_node, next_wieght in trees[cur_node] :
      if visit[next_node] == -1 :
        visit[next_node] = cur_weight + next_wieght
        dq.append((next_node,visit[next_node]))

  return visit

distance = bfs(1)
print(max(bfs(distance.index(max(distance)))))