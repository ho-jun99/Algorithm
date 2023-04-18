import sys
from collections import defaultdict
from collections import deque

RED = 1
BLUE = -1


def solve():
  V, E = map(int, sys.stdin.readline().split())  # V 정점의 개수, E 간선의 개수
  graph = defaultdict(list)
  visit = [0] * (V + 1)  # 0 == 방문X , 1 == RED , -1 == BLUE
  for _ in range(E):
    a, b = map(int, sys.stdin.readline().split())
    # 양방향 연결
    graph[a].append(b)
    graph[b].append(a)

  # BFS를 이용해서 확인함.
  for i in range(1, V + 1):
    if visit[i] == 0:  # 방문하지 않은 그래프라면
      dq = deque()
      dq.append( (i, RED) )
      visit[i] = RED

      while len(dq) != 0:
        cur = dq.popleft()  # ( VERTEX, COLOR )
        # print(cur)
        for neighbor in graph[cur[0]]:  # 인접한 이웃 노드들
          ## 다음 색칠될 색을 미리 확정해주기
          if cur[1] == RED:
            color = BLUE
          else:
            color = RED
          next = (neighbor, color)
          ## --- ##

          if visit[neighbor] == 0:  # 해당 이웃을 방문하지 않았다면
            dq.append(next) # 큐에 추가
            visit[next[0]] = next[1] # 색칠하기
            # print("here")
          else : # 방문 했었다면, 이웃 노드의 색은 next색이어야함
            if visit[neighbor] != next[1] :
              print("NO")
              return

  print("YES")
  return


K = int(sys.stdin.readline())
for _ in range(K):
  solve()
