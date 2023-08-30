import sys
from collections import deque

def print2D(arrs) :
  print("---")
  for i in arrs :
    print(i)

DIR_RIGHT = 1
DIR_LEFT = 2
DIR_UP = 3
DIR_DOWN = 4

dirs = [
  # 우,좌,상,하
  (0, 0), (0, 1), (0, -1), (-1,0), (1,0)
  ]

class Pawn() :
  def __init__(self,row,col,DIR,id):
    self.row = row
    self.col = col
    self.dir = DIR
    self.id = id

  def reverseDir(self):
    if self.dir == 1 :
      self.dir = 2
    elif self.dir == 2 :
      self.dir = 1
    elif self.dir == 3 :
      self.dir = 4
    elif self.dir == 4 :
      self.dir = 3

  def move(self,row,col):
    self.row = row
    self.col = col

  def __str__(self):
    return f"{id}"


# N : 체스판의 크기, K : 말의 개수
N,K = map(int,sys.stdin.readline().split())
board = list()
# 기물 모음
pawns = list()

for _ in range(N) :
  line = list(map(int,sys.stdin.readline().strip().split()))
  for i in range(len(line)) :
    dq = deque()  # 보드에 폰들을 기록하기 위해서
    line[i] = [line[i],dq]
  board.append(line)


for id in range(K) :
  row,col,dir = map(int,sys.stdin.readline().split())
  # 1 부터 시작하기 때문에 값 보정
  row -= 1
  col -= 1
  p = Pawn(row,col,dir,id+1)
  board[row][col][1].append(p)
  pawns.append(p)

# 말이 4개 이상 쌓이는 순간 게임이 종료 된다. ( 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력 )
COLOR_WHITE = 0 # 흰색인경우  ( 0 ) => 그냥 이동
COLOR_RED = 1 # 빨간색인경우 ( 1 ) => 이동한 후 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
COLOR_BLUE = 2 # 파란색인경우 ( 2 ) => 이동 방향을 반대로 하고 한 칸 이동한다. 이동하려는 칸이 파란색인 경우에는 이동하지 않는다.
OUT = 2 # 체스판을 벗어나는 경우 => 파란색(2)와 같은 처리


# 위에 얹혀지는 것을 어떻게 표현 할 것인가?
  # 링크드 리스트 ? => 기물이 최대 10개니까 그냥 반복문 돌려도 될듯 하다.
  # 보드에 일단 말을 기입해야지, 얹히든 뭐를 할 수 있다.
  # 보드에 말들이 필요하긴 하다. ( deque )

time = 0
while True :
  time +=1
  if time > 1000 :
    # 실패 종료 조건
    print(-1)
    break

  # 폰들이 번호에 따라서 하나씩 이동해야 한다.
  for pawn in pawns :
    # 움직이기 전에 위에 말들이 있는지 확인해야 한다.
    dq = board[pawn.row][pawn.col][1] # 현재 폰의 dq
    curPawnIdx = dq.index(pawn) # 현재 폰의 인덱스

    # 폰이 이동할 다음 칸을 구한다.
    nextRow = pawn.row + dirs[pawn.dir][0]
    nextCol = pawn.col + dirs[pawn.dir][1]

    # 임시로 tempDq를 만들고 해당 extend하는 방식을 사용하자.
    tempDq = deque()

    if 0 <= nextRow < N and 0 <= nextCol < N and board[nextRow][nextCol][0] != COLOR_BLUE:
      nextDq = board[nextRow][nextCol][1]

      for i in range(curPawnIdx, len(dq)):
        popedPawn = dq.pop()
        popedPawn.move(nextRow, nextCol)
        tempDq.appendleft(popedPawn)

      # 범위 안일경우
      if board[nextRow][nextCol][0] == COLOR_WHITE :
        # 이동 시킨다.
        nextDq.extend(tempDq)
      elif board[nextRow][nextCol][0] == COLOR_RED :
        # 역전시키고 이동 한다.
        tempDq.reverse()
        nextDq.extend(tempDq)

      # 종료조건
      if len(nextDq) >= 4 :
        print(time)
        exit()

    else :
      pawn.reverseDir() # 방향을 바꾼다.
      # 다음 이동해야할 곳을 **다시** 구한다.
      nextRow = pawn.row + dirs[pawn.dir][0]
      nextCol = pawn.col + dirs[pawn.dir][1]
      # print(f"before : {pawn.row,pawn.col} after : {nextRow,nextCol} afterDir : {dirs[pawn.dir]} / " , end=" ")

      # 다음 이동하는 곳이 파란색이 아니고 범위 안에 있으면
      if 0 <= nextRow < N and 0 <= nextCol < N and board[nextRow][nextCol][0] != COLOR_BLUE:
        nextDq = board[nextRow][nextCol][1]

        for i in range(curPawnIdx, len(dq)):
          popedPawn = dq.pop()
          popedPawn.move(nextRow, nextCol)
          tempDq.appendleft(popedPawn)

        # 범위 안일경우
        if board[nextRow][nextCol][0] == COLOR_WHITE:
          # 이동 시킨다.
          nextDq.extend(tempDq)
        elif board[nextRow][nextCol][0] == COLOR_RED:
          # 역전시키고 이동 한다.
          tempDq.reverse()
          nextDq.extend(tempDq)

        # 종료조건
        if len(nextDq) >= 4:
          print(time)
          exit()

      else:
        # 이번에는 아무것도 하지 않는다.
        pass
    # print(time,end=" ")
    # print2D(board)