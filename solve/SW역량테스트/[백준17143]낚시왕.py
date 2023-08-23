import sys

def print2D(arrs) :
    print("--")
    for i in arrs :
        print(*i)

DIR_UP = 1
DIR_DOWN = 2
DIR_RIGHT = 3
DIR_LEFT = 4
STATE_LIVE = 1
STATE_DIE = 0

dirs = [
    (0,0),(-1,0),(1,0),(0,1),(0,-1)
]

sharks = list()
R,C,M = map(int,sys.stdin.readline().split())
board = [ [-1 for i in range(C)] for j in range(R)]

class Shark() :
    def __init__(self,row,col,speed,dir,size):
        self.row = row
        self.col = col
        self.speed = speed
        self.dir = dir
        self.size = size
        self.life = STATE_LIVE

    def setLocation(self,row,col,d):
        self.row = row
        self.col = col
        self.dir = d
    def getLocation(self):
        return (self.row,self.col)

    def kiiShark(self):
        self.life = STATE_DIE
        self.row = -1
        self.col = -1
        self.dir = -1

    def move(self):
        moveCount = self.speed
        curRow = self.row; curCol = self.col
        while moveCount != 0 :
            dirRow, dirCol = dirs[self.dir]
            nextRow = curRow + dirRow
            nextCol = curCol + dirCol

            if 0 <= nextRow < R and 0 <= nextCol < C :
                curRow = nextRow
                curCol = nextCol
                moveCount -=1
            else :
                # 범위를 벗어나는 경우
                # 방향 변경해주고 moveCount를 차감하지 않음으로써 다음번에 계산 가능하도록 함
                if self.dir == DIR_UP :
                    self.dir = DIR_DOWN

                elif self.dir == DIR_DOWN :
                    self.dir = DIR_UP

                elif self.dir == DIR_LEFT :
                    self.dir = DIR_RIGHT

                elif self.dir == DIR_RIGHT :
                    self.dir = DIR_LEFT

        self.row = curRow
        self.col = curCol
        return (self.row,self.col,self.dir)

    def __str__(self):
        return f"(speed : {self.speed} size : {self.size} ) "

    def isSharkLive(self):
        if self.life == STATE_LIVE :
            return True
        else :
            return False


for id in range(M) :
    #(r,c), s=속력, d=이동방향, z=크기
    r,c,s,d,z = map(int,sys.stdin.readline().split())
    # 문제는 1행1열부터 시작하기 때문이 값에 대한 보정이 이루어져야 한다.
    r -=1; c-=1;
    shark = Shark(r,c,s,d,z)
    sharks.append(shark)
    board[r][c] = id


totalSize = 0
# 낚시왕이 한칸씩 이동하면서 맨오른쪽 칸에 도착할때까지 진행한다.
# 즉 열의 개수만큼 이동해야 한다.
for masterCol in range(C) :
    # 현재 위치에서 땅과 제일 가까운 상어를 잡는다.
    for searchRow in range(R) :
        if board[searchRow][masterCol] != -1 :
            # -1이 아니라면 그 위치에는 상어가 존재한다.
            sharkId = board[searchRow][masterCol]
            targetShark = sharks[sharkId]
            # 잡은 상어의 크기를 더해준다.
            totalSize += targetShark.size
            # 해당 위치에 상어 표기를 없앤다.
            board[searchRow][masterCol] = -1
            # 상어를 죽여준다.
            targetShark.kiiShark()
            break

    # 현재 살아있는 상어들로 하여금 위치 이동을 시켜줘야 한다.
    afterBoard = [ [-1 for i in range(C)] for j in range(R)]
    for id,shark in enumerate(sharks) :
        if shark.isSharkLive() :
            # 현재 좌표를 지워줄 필요가 없다. 결과는 새로운 afterboard로 이동할거니까
            # 이동 시킨다. move를 수행하면서 shark의 위치 및 dir은 알아서 바꿔진다.
            movedRow,movedCol,movedDir = shark.move()
            # 이동 후 좌표로 업데이트 하기전에 해당 좌표의 상어와 크기 비교를 해서 업데이트 해야한다.
            if afterBoard[movedRow][movedCol] != -1 :
                beforeShark = sharks[afterBoard[movedRow][movedCol]]
                if beforeShark.isSharkLive() :
                    # 현재 상어가 더 크다면, 이전상어를 죽이고, board를 현재상어의 값으로 최신화 한다.
                    if shark.size > beforeShark.size :
                        afterBoard[movedRow][movedCol] = id
                        beforeShark.kiiShark()
                        # print("beforeShark was killed! : "  + str(beforeShark) + "killed by " + str(shark))

                    # 기존에 존재하던 상어가 더 크다면 현재 상어를 죽인다.
                    if shark.size < beforeShark.size :
                        shark.kiiShark()
                        # print("curShark was killed! : " + str(shark) + "killed by " + str(beforeShark) )

            else :
                # 이동 위치에 상어가 없을때는 그냥 이동시켜주자.
                afterBoard[movedRow][movedCol] = id

    # 업데이트된 보드를 현재보드로 바꿔주자
    board = afterBoard
    # print2D(board)
    # print("totalSize : " , totalSize, "mastCol : ", masterCol)
    # print()

print(totalSize)