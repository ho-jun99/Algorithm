import sys
from collections import deque
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())

dirs = [
  -1, 1
  ]

visit = [False] * (100_001)
visit[N] = True
dq = deque()
dq.append((N, 0))
counter = defaultdict(int)

cnt = 0
minimum_step = -1
while len(dq) != 0:
  pos, step = dq.popleft()
  visit[pos] = True

  if pos == K :
    counter[step] += 1

  # 곱하기로 이동할 경우
  next = pos * 2
  if 0 <= next <= 100_000 and visit[next] == False:
    dq.append((next, step + 1))

  # -1 또는 +1로 이동하는 경우
  for dir in dirs:
    next = pos + dir
    if 0 <= next <= 100_000 and visit[next] == False:  # 방문 가능하는 곳이면 방문시킨다.
      dq.append((next, step + 1))

# 최단거리기이기 때문에 counter가 맨앞일 경우임
for item in counter.items() :
  print(item[0])
  print(item[1])
  exit()