'''
  - 노드간 여러개 엣지가 존재 할 수 있다.
  - 양방향 다리이다.
  - DFS + 백트래킹을 활용해서 길의 최대값을 구한다 -> 시간초과 or 메모리 초과
  - 모든 경우의 수를 구하고 거기서 최대값을 구한다 -> 시간초과 or 메모리 초과
  - 이분탐색 시간복잡도 -> O(logN)
    - 0 ~ 10억의 경우의 수에서 해당 값을 경로가 넘어버리는지 아닌지를 확인한다
    - O(log 10억) 은
    - 도착점까지의 길은 무조건 있다.
'''
import sys
from collections import defaultdict
from collections import deque

MAX = 1_000_000_000  # 10억
N, M = map(int, sys.stdin.readline().split())  # N : 노드, M : 엣지
graph = defaultdict(list)
# graph = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b, c = map(int, sys.stdin.readline().split())
  # 양방향 다리
  graph[a].append((b, c))
  graph[b].append((a, c))


start, end = map(int, sys.stdin.readline().split())
left = 1
right = MAX
result = -1
while left <= right:
  mid = (left + right) // 2  # 이 값이 중량 값임, 이값으로 도착이 가능한지 판단하면 됨

  # 도착점까지의 길이 무조건 있기 때문에, mid값보다 크거나 같은 간선만 선택해서 가자
  dq = deque()
  dq.append(start)
  visit = [False] * (N + 1)
  visit[start] = True
  isFinish = False

  while len(dq) != 0:
    cur = dq.popleft()
    for neighbor in graph[cur]:  # neighbor : (vertex, cost)
      if mid <= neighbor[1]:
        if visit[neighbor[0]] == False:  # 방문했던 곳이 아니라면
          visit[neighbor[0]] = True
          dq.append(neighbor[0])

          if neighbor[0] == end:  # 도착했으면, 범위를 키워봄
            left = mid + 1
            isFinish = True
            dq.clear()
            result = mid
            break
  if not isFinish :
    right = mid - 1  # 도착을 못했기 때문에 범위를 줄임

print(result)


# -- 재귀문 작성시 메모리 초과 --
# def binarySerach(left, right):
#   global start, end, N
#   if left == right:
#     return left
#
#   mid = (left + right) // 2  # 이 값이 중량 값임, 이값으로 도착이 가능한지 판단하면 됨
#
#   # 도착점까지의 길이 무조건 있기 때문에, mid값보다 크거나 같은 간선만 선택해서 가자
#   dq = deque()
#   visit = [False] * (N + 1)
#   visit[start] = True
#   dq.append(start)
#
#   while len(dq) != 0:
#     cur = dq.popleft()
#
#     for neighbor in graph[cur]:  # neighbor : (vertex, cost)
#       if mid <= neighbor[1]:
#         if visit[neighbor[0]] == False:  # 방문했던 곳이 아니라면
#           visit[neighbor[0]] = True
#           dq.append(neighbor[0])
#           if neighbor[0] == end:  # 도착했으면 범위를 키워봄
#             dq.clear()
#             return binarySerach(mid, right)
#   dq.clear()
#   return binarySerach(left, mid - 1)  # 도착을 못했기 때문에 범위를 줄임
# print(binarySerach(1,MAX))

# -- 실패 풀이--
# DFS를 이용해서 도착점까지 도착하는 모든 경우의 수를 다 구하는데
# 도착할때마다 거쳐온 간선에서의 최소 중량을 기록하고,
# 백트래킹으로 탐색할때 간선이 최소 중량보다 더 작아지면 그 길은 폐쇄 시켜 버린다.
# visit = [False] * (N+1)
# visit[start] = True
# result = -1
# isFirst = True

# def dfs(node,minimum) :
#   global result
#   global isFirst
#   if node == end :
#     result = max(result,minimum)
#     isFirst = True
#     return
#   # DFS 수행 + 백트래킹
#   for next in graph[node] :
#     if isFirst and visit[next[0]] == False :
#       visit[next[0]] = True
#       dfs(next[0], min(minimum, next[1]))
#       visit[next[0]] = False
#
#     elif isFirst == False and visit[next[0]] == False and result <= minimum :
#         visit[next[0]] = True
#         dfs(next[0], min(minimum, next[1]))
#         visit[next[0]] = False
#
# dfs(start,float('inf'))
# print(result
