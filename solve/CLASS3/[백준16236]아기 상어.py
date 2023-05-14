'''
  - BFS 단위를 잘 쪼개자. BFS를 소규모 단위로 쪼개서 끝내버릴 수록 코드짜기가 수월한거 같다.
  - BFS 에서 상태단위를 관리하기 위해서는, 큐에 담아서 뽑아서 계속 유지하고 업데이트 해야한다.
  - 이동한 경로를 0으로 표기해주자
  - 최소값 단위로 뽑아쓴다면 heap을 쓰면 더 빠를거 같다. 물고기 관리하는 fish배열을 heap으로 관리해볼까?
'''
import sys
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


## -- 고민했던 조건 들 -- ##
# # 종료조건
# # 상어가 더이상 먹을 물고기가 없으면 종료되어야함
# # 이걸 탐색으로 스스로 종료되게 할지 ?
# # 탐색 시작전에 딕셔너리에서 자기 아래것들의 숫자를 돌려서 찾을지 ?
# # 탐색조건
# # 거리가 가까운 물고기라면, 가장 위에 있는 그다음으로는 가장 왼쪽에 있는 물고기를 먼저 먹는다.
# # 가장 가까운 위에서부터 먹고 같으면 왼쪽부터 먹는다는 표현이 이해가 잘 안간다.
# # BFS로 이동순서를 정의해주는게 아닌가?
# # 우선순위를 줘야한다.
#
# # BFS를 매턴마다 돌리자
# # 턴은 물고기를 먹을때
