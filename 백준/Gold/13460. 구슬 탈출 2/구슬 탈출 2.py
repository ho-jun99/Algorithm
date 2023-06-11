import sys
from collections import deque

def print2D(arr) :
  for i in arr :
    print(i)
  print()

N,M = map(int,sys.stdin.readline().split())
board = list()

red = (-1,-1)
blue = (-1,-1)
end = (-1,-1)
RED = "R"
BLUE = "B"
for row in range(N) :
  line = list(sys.stdin.readline().strip())
  board.append(line)
  for col,item in enumerate(line) :
    if item == 'R' :
      red = (row,col,RED)
    if item == 'B' :
      blue = (row,col,BLUE)
    if item == 'O' :
      end = (row,col)
# print2D(board)

# 상, 우, 하, 좌
dirs = [
  (-1,0), (0,1), (1,0), (0,-1)
  ]

# 이동방향에 대해서 R이 먼저 움직여야 하는지 B가 먼저 움직여야 하는지에 대한 판단이 필요함
  # 예를들어서 행이동을 하려고 할때 , R과 B과 같은 행에 있다면 조건을 두고 이동해야함, 열이동도 똑같다.
# DFS가 유리할지 BFS가 유리할지에 대한 생각도 해봐야한다.
  # 최단거리니까 BFS가 더 유리하다
# 이동하는 하나의 단위를 틱이라고 했을때, 해당 틱에 Red와 Blue를 두개다 저장해야 할 듯 함.
# 방문한거 또 방문하지 말라는 법이 없는 문제이다. => visit관리 할 필요 없음
  # 그냥 실시간으로 board판만 잘 초기화 시키면 될 듯 함

dq = deque()
tick = (red,blue,1)
# board에서 RED공과 BLUE공의 위치를 .으로 바꾸어 놓는다.
board[red[0]][red[1]] = '.'
board[blue[0]][blue[1]] = '.'

# print2D(board)


cnt = 0
dq.append(tick)
while len(dq) != 0 :
  ballA,ballB,times = dq.popleft()
  for index,dir in enumerate(dirs) :
    first = ballA; second = ballB
    if (index == 1 or index == 3)  :
      if ballA[0] == ballB[0] : # 같은 행에 있을 경우 => 좌우만 영향을 받는다 => 우 : 1, 좌 : 3
        if ballA[1] < ballB[1] : # A공이 왼쪽에 있는 경우
          if index == 1 :
            first = ballB; second = ballA
          else :
            first = ballA; second = ballB
        else : # A공이 오른쪽에 있는 경우
          if index == 1:
            first = ballA; second = ballB
          else:
            first = ballB; second = ballA

    elif (index == 0 or index == 2) :
      if ballA[1] == ballB[1] : # 같은 열에 있을 경우 => 상,하만 영향을 받는다 => 상:0, 하: 2
        if ballA[0] < ballB[0] : # A공이 아래에 있는 경우
          if index ==0 :
            first = ballA; second = ballB
          else :
            first = ballB; second = ballA
        else: # A공이 위에 있는경우
          if index == 0 :
            first = ballB; second = ballA
          else :
            first = ballA; second = ballB

    # 여기까지 볼이 어떤거 먼저 이동해야하는지 정리가 끝남.
    # 여기서 first볼을 먼저 dir방향으로 벽이나올때까지 굴린다
    # 그다음에 second볼을 굴린다.

    row_first, col_first, color_first = first
    while True :
      next = (row_first+dir[0], col_first + dir[1])
      if 0 <= next[0] < N and 0<= next[1] < M : # 이동 범위 안이면서
        if board[next[0]][next[1]] == '.' : # 이동 가능한 지점이라면
          row_first = next[0]; col_first = next[1]
        elif board[next[0]][next[1]] == 'O' : # 빠지는 지점이면 !
          row_first = next[0]; col_first = next[1]
          break
        else :
          break
      else :
        break

    # 구멍에 빠진게 아니라면 해당 위치에 구슬을 표기해준다.
    # if row_first != end[0] and col_first != end[1]: -> 이 조건식에 무슨 문제가 있는거야?!
    if not(row_first == end[0] and col_first == end[1]) :
      board[row_first][col_first] = color_first
      # print(f"2D print : {row_first,col_first}, 기울임 방향 : {index}")
      # print2D(board)

    row_second, col_second, color_second = second
    while True:
      next = (row_second + dir[0], col_second + dir[1])
      if 0 <= next[0] < N and 0 <= next[1] < M :  # 이동 범위 안이면서
        if board[next[0]][next[1]] == '.' :  # 이동 가능한 지점이라면
          row_second = next[0]; col_second = next[1]
        elif board[next[0]][next[1]] == 'O':
          row_second = next[0]; col_second = next[1]
          break
        else :
          break
      else :
        break



    # 구슬 표기를 원상복귀 해준다.
    # 구멍에 빠진게 아니라면 해당 위치에 구슬을 표기해준다.
    if not(row_first == end[0] and col_first == end[1]):
      board[row_first][col_first] = '.'

    # 각각 구슬들의 위치를 비교해보고 큐에 넣을지 종료할것인지 결정한다.
    # 두개가 같은 위치가 아니면서(동시에 빠진게 걸러짐) 둘중에 하나는 목적지에 도착했을 경우

    # print(f"times : {times} , first : {row_first, col_first, color_first} , second : {row_second, col_second, color_second},기울임 방향 : {index} from : {first},{second}")

    # if (row_first != row_second and col_first != col_second) and ((row_first==end[0] and col_first ==end[1]) or (row_second==end[0] and col_second ==end[1])):
    #   if times <= 10 : # 10 이하이면
    #     print(times)
    #     dq.clear()
    #     exit()

    if color_first == BLUE :
      if row_first == end[0] and col_first == end[1] :
        continue
    if color_second == BLUE :
      if row_second== end[0] and col_second == end[1] :
        continue

    if color_first == RED :
      if row_first == end[0] and col_first == end[1] :
        print(times)
        exit()
    if color_second == RED :
      if row_second== end[0] and col_second == end[1] :
        print(times)
        exit()

    if (row_first == first[0] and col_first == first[1]) and (row_second == second[0] and col_second == second[1]) :
      # print(f"{first} :{row_first,col_first,color_first}, {second}, {row_second,col_second,color_second}")
      continue

    # 어느 하나도 구멍에 빠지지 않았을때는 이제 큐에 넣어줌
    if not((row_first == end[0] and col_first == end[1]) and (row_second ==end[0] and col_second==end[1])) and times < 10:
      dq.append(((row_first, col_first, color_first), (row_second, col_second, color_second), times + 1))


print(-1)