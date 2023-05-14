import sys
from collections import deque


def show2D(arr):
  for i in range(len(arr)):
    print(*board[i])


N, M = map(int, sys.stdin.readline().split())
board = list()

dirs = [
  (-1, 0), (0, 1), (1, 0), (0, -1)
  ]

candidaties = list()
for _ in range(N):
  line = list(map(int, sys.stdin.readline().split()))
  board.append(line)

# 치즈의 외곽과 치즈의 외부를 어떻게 구별할 것인가?
  # 내부공기인지의 여부..를 어떻게 알 수 있을까?
  # 해당 좌표에서 4방향을 찍고 내부인지 외부인지 판단해야 할듯
  # 가장자리에는 치즈가 놓이지 않는다. 가장자리는 무조건적으로 외곽이지 않을까? <- 채택
# 동시에 없애야한다.
  # 하나씩 순차적으로 체크하고 없애버리면 영향을 끼치게 된다.
  # 매 탐색 시작시 마다 내 외부를 결정해야하는데.. 이 방법이 맞을까 싶다.

timer = 0
while True:
  # board[0][0]으로 완전탐색 한번 돌려버리고 외곽 외곽은 -1, 내부는 0으로 마킹하자
  dq = deque()
  dq.append((0, 0))  # 첫 가장자리
  end_cnt = 1  # 이게 N*M 되면 종료조건임 ( 모든곳이 다 외곽이라는 뜻 )
  board[0][0] = -1  # 방문표시

  while len(dq) != 0:
    row, col = dq.popleft()
    for dir in dirs:
      next_row = row + dir[0]
      next_col = col + dir[1]
      if 0 <= next_row < N and 0 <= next_col < M:
        if board[next_row][next_col] == 0:  # 치즈 있는 곳이 아니라면
          board[next_row][next_col] = -1  # 방문표시
          dq.append((next_row, next_col))
          end_cnt += 1

  if end_cnt == N * M:  # 모든곳이 다 외곽이기 때문에 종료조건이 된다.
    break

  # 치즈를 녹인다.
  for row in range(N) :
    for col in range(M) :
      if board[row][col] == 1 :
        air_cnt = 0
        for dir in dirs :
          next_row = row + dir[0]
          next_col = col + dir[1]
          if 0<= next_row < N and 0<= next_col < M :
            if board[next_row][next_col] == -1 : # 외부 공기이면
              air_cnt+=1

        if 2<= air_cnt : # 접촉 외부 공기가 2이상일때
          candidaties.append((row,col))

  # 후보군에서 뽑아서 그 자리를 0으로 만든다. ( 치즈를 녹이를걸 후행시키기 위해서 )
  for candidate in candidaties :
    board[candidate[0]][candidate[1]] = 0

  # 다시 원상복귀를 시킨다.
  for row in range(N):
    for col in range(M):
      if board[row][col] == -1:
        board[row][col] = 0
  timer += 1
  candidaties.clear()

print(timer)