'''
  - BFS를 이용한 전형적인 풀이 같다.
'''
import sys
from collections import deque
from collections import defaultdict

A, B = map(int, sys.stdin.readline().split())
dq = deque()
visit = defaultdict(bool)
dq.append((A, 1))
visit[A] = True  # 초기 방문

while len(dq) != 0:
  cur = dq.popleft()  # ( node, cnt )

  next1 = (cur[0] * 2, cur[1] + 1)
  next2 = ((cur[0] * 10) + 1, cur[1] + 1)

  if next1[0] == B or next2[0] == B:
    print(next1[1])
    exit()

  if visit[next1[0]] == False and next1[0] <= B:
    dq.append(next1)
    visit[next1[0]] = True

  if visit[next2[0]] == False and next2[0] <= B:
    dq.append(next2)
    visit[next2[0]] = True

print(-1)
