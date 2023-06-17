import sys
from collections import deque

LEFT = -1
RIGHT = 1

# N극은 0, S극은 1
A = deque(list(map(int, sys.stdin.readline().strip())))
B = deque(list(map(int, sys.stdin.readline().strip())))
C = deque(list(map(int, sys.stdin.readline().strip())))
D = deque(list(map(int, sys.stdin.readline().strip())))

arrs = [[], A, B, C, D]

# 회전 횟수
K = int(sys.stdin.readline())

def rotate(idx, dir):
  global arrs, LEFT, RIGHT
  if dir == LEFT:
    arrs[idx].append(arrs[idx].popleft())
  if dir == RIGHT:
    arrs[idx].appendleft(arrs[idx].pop())


for _ in range(K):
  idx, dir = map(int, sys.stdin.readline().split())

  # bfs처럼 양옆 톱니들을 비교해야한다. (전파)
  dq =deque()
  dq.append((idx,dir)) # 톱니, 회전방향( 반대방향으로 회전시켜야 하기 때문에 )
  visit = [False] * 5
  visit[idx] = True
  l = deque()
  r = deque()
  while len(dq) !=0 :
    midx, mdir = dq.pop()
    nl = midx - 1; nr = midx + 1  # 양옆 톱니

    if 1 <= nl <= 3 and visit[nl] == False:
      if arrs[midx][6] != arrs[nl][2] :
        # rotate(nl,-1*mdir) # 반대방향으로 회전시킨다.
        visit[nl] = True # 방문처리
        dq.append((nl,-1*mdir))
        l.append((nl,-1*mdir))

    if 2 <= nr <= 4 and visit[nr] == False:
      if arrs[midx][2] != arrs[nr][6]:
        # rotate(nr, -1*mdir)  # 반대방향으로 회전시킨다.
        visit[nr] = True  # 방문처리
        dq.append((nr, -1*mdir))
        r.append((nr, -1*mdir))

  for i in range(len(l)) :
    midx, mdir = l.pop()
    rotate(midx,mdir)
  for i in range(len(r)) :
    midx,mdir = r.pop()
    rotate(midx,mdir)
  rotate(idx, dir) # 톱니 회전
  # print(arrs)



# N극은 0, S극은 1
# print(arrs)

result = 0
for idx in range(1,5) :
  if arrs[idx][0] == 1 :
    result += pow(2,idx-1)

print(result)