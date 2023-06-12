import sys
from collections import deque

def print2D(arr) :
  for i in arr :
    print(i)
  print()

LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'
DIR_DEFAULT = (0,1,RIGHT)

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())  # 사과의 개수
apples = list()

visit = [['.'] * (N) for _ in range(N)]

def changeDir(fr,to) :
  if fr == LEFT :
    if to == 'L' :
      return (1,0,DOWN)
    if to == 'D' :
      return (-1,0,UP)

  if fr == RIGHT :
    if to == 'L' :
      return (-1,0,UP)
    if to == 'D' :
      return (1,0,DOWN)

  if fr == UP :
    if to == 'L' :
      return (0,-1,LEFT)
    if to == 'D' :
      return (0,1,RIGHT)

  if fr == DOWN :
    if to == 'L' :
      return (0,1,RIGHT)
    if to == 'D' :
      return (0,-1,LEFT)

for _ in range(K):
  row, col = map(int, sys.stdin.readline().split())
  visit[row-1][col-1] = "A"

L = int(sys.stdin.readline().strip())  # 뱀의 방향 회전 횟수
moves = list()

for _ in range(L):
  time, turn = sys.stdin.readline().split()
  moves.append((int(time), turn))

# 자신의 몸에 부딪히면 게임 종료
# 벽에 부딪히면 게임 종료

# 생각해야할 것
# 보드를 그려서 구해야할까? 아니면 그냥 로직적으로 처리할 수 있을까
# 몸길이로 자폭하는 경우만 없다면 그냥 짜도 될텐데..



snakes = deque()
snakes.append((0, 0))
visit[0][0] = "#"
move_top = 0
t = 0
while True:
  t += 1
  snake_head = (snakes[0][0],snakes[0][1]) # 스네이크의 헤드에서 진행방향으로 추가해야함

  tail = snakes.pop()  # (row,col)

  next_head = (snake_head[0] + DIR_DEFAULT[0], snake_head[1] + DIR_DEFAULT[1])
  if (0 <= next_head[0] < N and 0 <= next_head[1] < N) and (visit[next_head[0]][next_head[1]] != "#") :  # 범위 안이면서  몸통이 없는 곳이라면
    visit[tail[0]][tail[1]] = '.'  # 꼬리 부분 뜯기
    if visit[next_head[0]][next_head[1]] == "A" : # 사과를 만나면, 꼬리를 추가시킨다.
      snakes.append((tail[0],tail[1]))
      visit[tail[0]][tail[1]] = '#'

    snakes.appendleft(next_head)
    visit[next_head[0]][next_head[1]] = '#'
  else:
    print(t)
    exit()

  # 시간에 따른 방향 전환
  if move_top < len(moves) :
    time,turn = moves[move_top]
    if time == t :
      DIR_DEFAULT = changeDir(DIR_DEFAULT[2],turn)
      move_top+=1

  # if move_top < len(moves) :
  #   print(t, moves[move_top])
  # print2D(visit)

