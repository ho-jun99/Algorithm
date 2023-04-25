# 크면 못지나감
# 같으면 지나감
# 작으면 먹음
# 거리가 같으면 위쪽 먼저 같으면 왼쪽에 있는 것
# 현재 자신의 크기만큼의 물고기를 먹으면 커

# 필요한 것
# 현재 물고기의 위치
# 크기별 물고기들의 갯수
import sys
from collections import deque

time = 0
n = int(sys.stdin.readline())
board = []
fishs = [0] * 7
shark = [2, 0]


def callMom():
  print(time)
  exit()


def isFishsEatChecking():  # 현재 물고기들 현황을 파악해서 먹을 수 있는 피시가 있는지
  cnt = 0
  for i in range(1, 7):
    if fishs[i] > 0:
      if shark[0] > i:
        cnt += 1
  if cnt == 0:
    return False
  else:
    return True


cur = (-1, -1)
for i in range(n):
  line = list(map(int, sys.stdin.readline().split()))
  temp = list()
  for item in line:
    temp.append([item, 0])
  board.append(temp)
  for index, item in enumerate(line):
    if item == 9:
      cur = (i, index)
      continue
    # print(item)
    fishs[item] += 1

# print(board)

# bfs로 돌아야함
# 4방향 탐색, 최단 거리에 있는거 찾기, 물고기 초기 값 2, 그쪽으로 이동 이동할때 i횟수 더해주기
# 틈틈히 피시 현황 관리하기

dirs = [
  (-1, 0), (0, -1), (1, 0), (0, 1)
  ]

# 4방향 탐색에 대해서 두번 돌기

dq = deque()
dq.append(cur)
board[cur[0]][cur[1]][0] = 0
board[cur[0]][cur[1]][1] = 1
print(board)
while isFishsEatChecking():
  cur = dq.popleft()  # 현재 위치
  # print(f"cur : {cur}")
  # 4방향 탐색 두번 돌기

  isEatFish = False
  for turn in range(2) :
    for dir in dirs:
      # 첫번째 탐색에서는 4방향에 먹을 수 있는 물고기가 있는지 확인
      next = (cur[0] + dir[0], cur[1] + dir[1])
      # print(f" turn : {turn}, next : {next}")
      if turn == 0 and 0 <= next[0] < n and 0 <= next[1] < n and shark[0] > board[next[0]][next[1]][0]:
        dq.clear() # 먹으면 큐 비우기
        dq.append(next)  # 이동하기
        shark[1] += 1  # 먹기
        isEatFish = True
        fishs[board[next[0]][next[1]][0]] -= 1  # 물고기 현황 업데이트
        board[next[0]][next[1]][0] = 0  # 그자리 0으로 만들기
        board[next[0]][next[1]][1] +=1  # 시간 업데이트

        if shark[1] == shark[0]:  # 상어 몸집 키워주기
          shark[0] += 1
          shark[1] = 0
        break

      if turn == 1:
        if board[next[0]][next[1]][1] == 0 and board[next[0][next[1]]][0] == shark[0] or board[next[0][next[1]]][0] == 0:  # 이동할 수 있는 곳이라면 이동하기
          dq.append(next) # 이동 하기
          board[next[0]][next[1]][1] +=1 # 방문 표시 및 프로시져
          isEatFish = False

    if isEatFish:
      break


print("end")