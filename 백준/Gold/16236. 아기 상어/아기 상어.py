import sys
from collections import defaultdict
from collections import deque


def print2D(arr):
  for row in range(N):
    for col in range(N):
      print(arr[row][col], end=" ")
    print()
  print()


N = int(sys.stdin.readline().strip())  # 공간의 크기
board = list()

dirs = [
  (-1, 0), (0, -1), (1, 0), (0, 1)
  ]

for _ in range(N):
  line = list(map(int, sys.stdin.readline().split()))
  board.append(line)

# 물고기통을 기준으로 한다
# 현재 시작점에서 BFS로 물고기 후보들을 구한다
# 구한 물고기 후보들에서 가장 거리가 가까운 순에서 맨위 맨 왼쪽에 있는 물고기를 첫번째로 꺼낸다
# 다시 탐색하고 물고기 후보가 없어지면 탐색을 종료한다.

start = (-1, -1)
for row in range(N):
  for col in range(N):
    if board[row][col] == 9:
      start = (0, row, col)  # 거리, 행, 열

fishes = list()
sstate = (2, 0, 0)  # ( 몸집, 먹은 물고기 수 , 이동한 칸 )
fishes.append((start, sstate))  # (거리, 행, 열), ( 몸집, 먹은 물고기 수 , 이동한 칸 )
total = 0
while len(fishes) != 0:
  fishes.sort(key=lambda x: (x[0][0], x[0][1], x[0][2]))  # 거리, 위치 순으로 정렬한다
  time, row, col = fishes[0][0]
  total += time
  state = fishes[0][1]
  fishes.clear()  # 물고기후보군 비우기
  cur = (row, col)
  visit = [[False] * N for _ in range(N)]
  visit[cur[0]][cur[1]] = True  # 방문처리
  board[cur[0]][cur[1]] = 0  # 시작점 초기화

  dq = deque()
  dq.append((cur[0], cur[1], 0))  # 행,열, 시작점에서부터 거리

  while len(dq) != 0:
    pos = dq.popleft()  # 현재 위치부터 BFS로 전역 탐색함
    for dir in dirs:
      next = (pos[0] + dir[0], pos[1] + dir[1])
      if 0 <= next[0] < N and 0 <= next[1] < N and not visit[next[0]][next[1]]:  # 범위 안이면서 방문하지 않은 곳이면

        if board[next[0]][next[1]] == 0 or board[next[0]][next[1]] == state[0]:  # 그냥 이동이 가능한 곳이면
          dq.append((next[0], next[1], pos[2] + 1))
          visit[next[0]][next[1]] = True  # 방문처리

        elif 0 < board[next[0]][next[1]] < state[0]:  # 먹을 수 있는 후보군 이면
          level = state[0]
          eatten = state[1] + 1
          if level == eatten:
            level += 1
            eatten = 0
          fishes.append(((pos[2] + 1, next[0], next[1]), (level, eatten, 0)))
          visit[next[0]][next[1]] = True
print(total)