import queue
import sys

# n 유저의 수, m 친구 관계
n,m = map(int,sys.stdin.readline().split())

net = [set() for i in range(n+1)]

for i in range(m) :
  first, second = map(int,sys.stdin.readline().split())
  net[second].add(first)
  net[first].add(second)

# before 가중치
# visit
# BFS

min_cnt = float('inf')
min_node = 0
for i in range(1,n+1) :
  que = queue.Queue()
  visit = [False] * (n+1)
  # 각 사람들 별로 케빈 베이컨의 수를 구함

  # bfs 수행,
  que.put(i)
  visit[i] = True
  weight = [0] * (n+1)
  while not que.empty() :
    cur = que.get()

    for j in net[cur] :
      if visit[j] : continue
      else :
        # 방문 처리 후, 큐에 넣어줌
        visit[j] = True
        weight[j] = weight[cur] + 1
        que.put(j)

  cur_cnt = 0
  for j in range(1,n+1) :
    cur_cnt += weight[j]
  # weight의 합계를 최소로 유지 시켜야함
  if min_cnt > cur_cnt :
    min_cnt = cur_cnt
    min_node = i

print(min_node)