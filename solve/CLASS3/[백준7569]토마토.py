#  M = 열
#  N = 행
#  H = 높이
# 1 = 익은 토마토, # 0 = 익지 않은 토마토, # -1 = 토마토가 들어있지 않은 칸
import queue
import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().strip().split())
# print(M, N, H)

tomatos = []

isRipen = True  # 처음부터 익은 토마토 판단 여부
for i in range(H):
  box = []
  for j in range(N):
    line = list(map(int, sys.stdin.readline().strip().split()))
    box.append(line)
    if isRipen and (0 in line):
      isRipen = False
  tomatos.append(box)

if isRipen:
  print(0)
  exit()

# q = queue.Queue()

dq = deque()
dir = [
  (-1, 0, 0), (1, 0, 0),
  (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1)
  ]

def initTomatos():
  for i in range(len(tomatos)):
    for j in range(len(tomatos[i])):
      for k in range(len(tomatos[i][j])):
        if tomatos[i][j][k] == 1:  # 시작위치
          # q.put((i, j, k,0))
          dq.append((i, j, k,0))

initTomatos()

maxDay = 0
while not len(dq) == 0:
  # cur = q.get() #(층, 행, 열)
  cur = dq.popleft()
  for nextDir in dir :
    next = (cur[0] + nextDir[0], cur[1] + nextDir[1], cur[2] + nextDir[2])
    if 0 <= next[0] < H and 0 <= next[1] < N and 0 <= next[2] < M : # 다음 범위 안에 있으면
      if tomatos[next[0]][next[1]][next[2]] == 0 : # 익지 않은 토마토 이면
        tomatos[next[0]][next[1]][next[2]] = 1
        mNext = (next[0],next[1],next[2], cur[3]+1)
        # print("mNext : " , mNext)
        maxDay = max(mNext[3],maxDay)
        # q.put(mNext)
        dq.append(mNext)

# 0이 존재하는지 확인
for i in range(len(tomatos)):
  for j in range(len(tomatos[i])):
    for k in range(len(tomatos[i][j])):
      if tomatos[i][j][k] == 0:  # 시작위치
        print(-1)
        exit()

print(maxDay)
# print(tomatos)