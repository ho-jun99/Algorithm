# 1 => 익은 토마토
# 0 => 익지 않은 토마토
# -1 => 토마토가 들어있지 않은 칸
import sys
from collections import deque

col,row = map(int,sys.stdin.readline().split())

tomatos = []

isRipen = True
for i in range(row) :
  line = list(map(int,sys.stdin.readline().split()))
  tomatos.append(line)
  if isRipen and 0 in line :
    isRipen = False


if isRipen :
  print(0)
  exit()

dirs = [(-1,0),(0,1),(1,0),(0,-1)]
dq = deque()

# 익은 토마토 큐에 넣기
for i in range(row) :
  for j in range(col) :
    if tomatos[i][j] == 1 :
      dq.append((i,j,0))

max = 0;
while len(dq) > 0 :
  cur = dq.popleft();
  for dir in dirs : # 다음으로 갈 곳 탐색
    next = (cur[0] + dir[0], cur[1] + dir[1], cur[2] + 1)
    if 0 <= next[0] < row and 0<= next[1] < col : # 범위 안에 있고
      if tomatos[next[0]][next[1]] == 0 : # 익지 않은 토마토 이면
        tomatos[next[0]][next[1]] = 1  # 방문 표시를 해준다.
        dq.append(next)
        if next[2] > max :
          max = next[2] # max를 갱신해준다.


# 토마토가 익지 않은 상태임을 확인한다.
for i in range(row) :
  for j in range(col) :
    if tomatos[i][j] == 0 :
      print(-1)
      exit()

# 토마토가 모두 익었다면 Max를 출력한다
print(max)