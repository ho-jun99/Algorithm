import queue
import sys

n,k = map(int,sys.stdin.readline().split())

# bfs로 이동하면 결국 1초에 이동하는 노드가 됨
# 1칸씩 계속해서 이동해보면서
# 찾는 값이 나오면 끝내고 그때의 카운트값을 반환

# 시작점 도착점이 시작부터 같을 경우
if n==k :
  print(0)
  exit(0)

que = queue.Queue()
visit = [False] * 100_001
weight = [0] * 100_001

que.put(n)
while not que.empty() :
  cur = que.get()

  for i in range(3) :
    next = 0
    if i == 0 :
      next = cur-1
    if i == 1 :
      next = cur +1
    if i == 2 :
      next = cur * 2

    if 100_000 >= next >= 0 :
      if not visit[next] :
        weight[next] = weight[cur] + 1
        visit[next] = True
        que.put(next)

      if next == k :
        print(weight[next])
        exit(0)