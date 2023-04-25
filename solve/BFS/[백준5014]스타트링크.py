import sys
from collections import deque

FAIL = "use the stairs"

F, S, G, U, D = map(int, sys.stdin.readline().split())
# 건물 높이 F
# 현재 위치 S
# 목표 지점 G
# 위로 U층 이동
# 아래로 D층 이동

dirs = [
  U, (-1*D)
]
# print(dirs)
visit = [False] * (F+1)
visit[0] = True # 0은 사용 안함

dq = deque()
dq.append((S,0)) # 현재 위치 삽입, 횟수
visit[S] = True

cnt = 0
while len(dq) != 0 :
  cur = dq.popleft()
  if cur[0] == G:
    print(cur[1])
    exit()
  # print(cur)

  for dir in dirs:
    next = (cur[0] + dir, cur[1] + 1 )
    if 1 <= next[0] <= F :
      if visit[next[0]] == False :
        # 다음으로 이동
        dq.append(next)
        visit[next[0]] = True

        # print("next : " , next)

        if next[0] == G :
          print(next[1])
          exit()

print(FAIL)


