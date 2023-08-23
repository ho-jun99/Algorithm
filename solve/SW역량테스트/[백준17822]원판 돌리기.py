import sys
from collections import deque

def print2D(arr):
  print("--")
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      print(arr[i][j], end=" ")
    print()
# 회전 방향 정의
TURN_RIGHT = 0 # 시계방향
TURN_LEFT = 1 # 반시계방향

# 탐색 방향 정의
dirs = [
    (-1,0),(0,1),(1,0),(0,-1)
]

board = list()
N,M,T = map(int,sys.stdin.readline().split())
for _ in range(N) :
    dq = deque()
    temp = list(map(int,sys.stdin.readline().split()))
    dq.extend(temp)
    board.append(dq)

# T번 회전시키는 커맨드를 수행함
for _ in range(T) :
    x,d,k = map(int,sys.stdin.readline().split())
    for i in range(x,N+1,x) : # x 배수
        idx = i-1 # 배열의 배수가 0부터 시작하기 떄문에 숫자를 보정해줌
        # 해당 인덱스에 관해서 로테이트를 k칸 수행해야함.

        if d == TURN_RIGHT : # (시계)
            board[idx].rotate(k)
        else : # TURN_LEFT (반시계)
            board[idx].rotate(-1*k)

    # 회전이 끝난 상태. 인접수에 대한 처리를 시작해야함.
    # BFS를 이용해서 인접수에 대한 검사를 진행한다.
    sum = 0
    postiveNumberCount = 0
    removeCount = 0
    for row in range(N) :
        for col in range(M) :
            curTarget = board[row][col]
            if curTarget == -1 :
                continue
            sum += board[row][col] if board[row][col] != -1 else 0 # 모든 곳을 순회하게 되기 떄문에
            postiveNumberCount += 1 if board[row][col] != -1 else 0 # 나눠줄 수
            dq = deque()
            dq.append([row,col])
            # dq가 빌때까지 BFS탐색을 시작한다.
            while len(dq) != 0 :
                _row,_col = dq.popleft()
                # 4방향을 살펴본다.
                for dir in dirs :
                    next = [_row+dir[0], _col+dir[1]]
                    # col값을 보정해준다
                    if next[1] == -1 :
                        next[1] = M-1
                    if next[1] == M :
                        next[1] = 0
                    if 0<= next[0] < N and 0<= next[1] < M and board[next[0]][next[1]] == curTarget :
                        # 인접한 수가 같은 수라면 지워준다.
                        # 여기서는 현재의 값이 지워진다.
                        board[_row][_col] = -1 # -1을 표기하여 지워준다
                        board[next[0]][next[1]] = -1 # 다음꺼도 미리 지워준다.
                        dq.append(next)
                        removeCount +=1

    if removeCount == 0 and postiveNumberCount > 0:
        # 지운게 하나도 없는경우 평균을 구해야 한다.
        _avg = sum / postiveNumberCount
        for subRow in range(N) :
            for subCol in range(M) :
                pivot = board[subRow][subCol]
                if board[subRow][subCol] != -1:
                    if pivot < _avg :
                        board[subRow][subCol] +=1
                    if pivot > _avg :
                        board[subRow][subCol] -= 1
    # print2D(board)

# 최종 합을 구해서 답을 구한다.
result = 0
for row in range(N) :
    for col in range(M) :
        result += board[row][col] if board[row][col] != -1 else 0

# print2D(board)
print(result)



# 런타임 에러 (ZeroDivisionError) 발생 어디서 발생하는걸까>?
# -> 모든곳이 -1로 다 변해버린 상황이라면 sum과 postiveCount가 초기값이 0인 상태이고 이럴떄 ZeroDivisionError가 발생할 것으로 추정 됨
# 그렇기 때문에 해당 경우를 처리하기 위해서 if removeCount == 0 and 'postiveNumberCount' > 0: 조건을 추가함.