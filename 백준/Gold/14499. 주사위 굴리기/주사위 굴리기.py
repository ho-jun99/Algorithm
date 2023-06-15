import copy
import sys


def print2D(arr) :
  for i in arr :
    print(i)
  print()

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4


dirs = [
  (-1,-1), (0,1), (0,-1),(-1,0),(1,0)
  ]

dice = [0,0,0,0,0,0]

# 지도크기, 좌표, 명령의 개수
N,M,x,y,K = map(int,sys.stdin.readline().split())

board = list()
for _ in range(N) :
  line = list(map(int,sys.stdin.readline().split()))
  board.append(line)

commands = list(map(int,sys.stdin.readline().split()))

# print2D(board)
# print(commands)

# 주사위를 굴렸을때
  # 이동한 칸에 쓰여있는수가 0이면, 주사위 바닥면에 쓰여 있는 수가 칸에 복사된다.
  # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위 바닥면으로 복사된다. 칸에 쓰여 있는 수는 0이 된다.


def diceTop() :
  global dice
  return dice[1]

def diceBottom() :
  global dice
  return dice[3]

def rollDice(state):
  global dice
  beforeDice = copy.copy(dice)

  if state == RIGHT :
    dice[1] = beforeDice[4]
    dice[5] = beforeDice[1]
    dice[3] = beforeDice[5]
    dice[4] = beforeDice[3]

  if state == LEFT :
    dice[1] = beforeDice[5]
    dice[4] = beforeDice[1]
    dice[3] = beforeDice[4]
    dice[5] = beforeDice[3]

  if state == UP :
    dice[1] = beforeDice[2]
    dice[0] = beforeDice[1]
    dice[3] = beforeDice[0]
    dice[2] = beforeDice[3]

  if state == DOWN :
    dice[1] = beforeDice[0]
    dice[2] = beforeDice[1]
    dice[3] = beforeDice[2]
    dice[0] = beforeDice[3]

for command in commands :
  dir = dirs[command]
  if 0 <= x+dir[0] < N and 0<= y +dir[1] < M: # 이동 가능할때
    x += dir[0]; y += dir[1]
    rollDice(command)
    if board[x][y] == 0 : # 이동한 칸의 바닥이 0 이면
      board[x][y] = diceBottom()
    else :
      dice[3] = board[x][y]
      board[x][y] = 0
    print(diceTop())