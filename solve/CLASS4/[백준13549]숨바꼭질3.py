'''
  - 수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구해라
  - BFS로 최단시간 탐색을 수행하자.
    - 각 초마다의 위치가 나오기 때문에, 무조건 찾는다는 조건이 내재되어 있어 보이기 때문에 가능할듯 보인다.
'''
import sys
from collections import deque
from collections import defaultdict

# N = 수빈이의 시작 위치
# K = 동생이 있는 위치
N,K = map(int,sys.stdin.readline().split())

dirs = [ -1, +1]
visit = defaultdict(bool)

dq = deque()
dq.append((N,0))
visit[N] = True

# 시작부터 일치할 수 있다.
if N == K :
  print(0)
  exit()

while len(dq) != 0 :
  x, step = dq.popleft()

  # 곱하기는 리스트에 못넣어서 따로 연산해줘야함
  if 0 <= x * 2 <= 100_000 and visit[x * 2] == False:
    if x * 2 == K:
      print(step)
      exit()
    visit[x * 2] = True
    dq.append((x * 2, step))

  for dir in dirs :
    next = x + dir
    if next == K :
      print(step+1)
      exit()
    if 0<= next <= 100_000 and visit[next] == False:
      visit[next] = True
      dq.append( (next, step+1 ) )