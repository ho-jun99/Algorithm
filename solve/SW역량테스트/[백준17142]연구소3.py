import copy
import sys
from itertools import combinations
from collections import deque

def print2D(arrs) :
    print("---")
    for i in range(len(arrs)) :
        print(arrs[i])

dirs = [
    (-1,0),(0,1),(1,0),(0,-1)
]

N,M = map(int,sys.stdin.readline().split())
board = list()
virus = list()
resultZeroCount = 0
for row in range(N) :
    line = list(map(int,sys.stdin.readline().split()))
    board.append(line)
    for col in range(N) :
        if line[col] == 2 :
            virus.append((row,col)) # 바이러스 후보군에 추가함
        if line[col] == 0 :
            resultZeroCount += 1

if resultZeroCount == 0 :
    print(0)
    exit()

virusCandidates = list(combinations(virus,M))
# 바이러스 최대 V개를 그룹에서 뽑아 후보군을 만들고
# 모두 활성화 시켜본다.
# 거기서 최소시간이랑 -1여부를 파악해야한다.
result = -9999
hitFlag = False
for virusCandidate in virusCandidates :
    dq = deque()
    copiedBoard = copy.deepcopy(board) # Board를 복사한다.
    hit = 0 # hit와 resultZeroCount가 똑같아야 다채운거임
    # 초기 모든 바이러스 시작위치를 비활성상태로 만들고
    for v in virus :
        # 바이러스를 구분해야한다. 바이러스를 지나갈 수 있기 때문에
        copiedBoard[v[0]][v[1]] = 8

    # 초기 시작위치를 지정해준다.
    for startRow,startCol in virusCandidate :
        dq.append((startRow,startCol,0)) # 시작위치
        # 초기 바이러스 시작위치를 활성화 값으로 바꿔준다.
        # 초기 위치를 0으로 설정해줄시, 0끼리 바로 옆이라면 문제가 발생
        # 뚫고 지나가버릴 수 있기 때문에 초기 위치를 -1로 표기함
        # 이동 카운트를 음수로 한다.
        copiedBoard[startRow][startCol] = 9
    submin = 0
    while len(dq) != 0 :
        if hit == resultZeroCount :
            # 모든 영역을 다 채운거임
            hitFlag = True
            result = max(result,submin)
            break
        curRow, curCol, step = dq.popleft()
        if result >= step :
            # 이미 최소값이 구해졌던 경우이기 때문에 earlystop시켜서 시간을 단축시킨다.
            break
        for dir in dirs :
            # 다음 예상 위치를 뽑아낸다.
            nextRow = curRow + dir[0]
            nextCol = curCol + dir[1]

            # 범위 안인지 확인을 한다.
            if 0<= nextRow < N and 0<= nextCol < N :
                # 이동가능한 곳이라면
                if copiedBoard[nextRow][nextCol] == 0 :
                    copiedBoard[nextRow][nextCol] = step-1
                    dq.append((nextRow,nextCol,step-1))
                    hit+=1
                    submin = min(submin,step-1)

                if copiedBoard[nextRow][nextCol] == 8 :
                    copiedBoard[nextRow][nextCol] = step - 1
                    dq.append((nextRow, nextCol, step - 1))
                    submin = min(submin, step - 1)

if hitFlag == False :
    print(-1)
else :
    print(abs(result))


