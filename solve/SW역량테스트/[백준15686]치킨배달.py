import sys
from collections import deque
from itertools import combinations

board = list()
N, M = map(int, sys.stdin.readline().split())
houses = list()
chicken = list()

def print2D(arr):
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      print(arr[i][j], end=" ")
    print()

# 조합의 문제이다.
# 치킨집 m개에 대해서 mC1 , mC2 , mC3 .... 해가면서 최솟값을 찾는다.
  # 이런문제에서 치킨집과 집을 다른 배열에 담는거와 같은 생각을 해볼 수 있다.
for _ in range(N):
  line = list(map(int, sys.stdin.readline().split()))
  board.append(line)

for row in range(N) :
  for col in range(N) :
    if board[row][col] == 1 :
      houses.append((row,col))
    if board[row][col] == 2 :
      chicken.append((row,col))

# print(chicken)
minumum = float('inf')
# 치킨집을 조합을 통하여 뽑는다 1가지, 2가지, 3가지,,, 최대 M가지
# 집은 치킨집 하나만 선택하면 되니까 집이 먼저 돈다
for i in range(1,M+1) :
  for combi in combinations(chicken,i) :
    # print(combi) # 치킨집의 조합이 뽑힌다. 이걸 토대로 최소거리를 구하자.
    sum = 0
    for house_pos in houses :
      mmin = float('inf')
      for chicken_pos in combi :
        mmin = min(mmin,abs(house_pos[0]-chicken_pos[0]) + abs(house_pos[1]-chicken_pos[1])) # 가장 가까운 치킨집 찾기
      # 해당집에 가장 가까운 치킨집을 찾았다면 sum에 더하기
      sum += mmin
    minumum = min(minumum,sum)
print(minumum)

# BFS로 각 치킨집에서 해당집으로까지의 거리를 구한다.

# dirs = [
#   (-1, 0), (0, 1), (1, 0), (0, -1)
#   ]

# distances = list()
# for row in range(N):
#   for col in range(N):
#     if board[row][col] == 2:  # 치킨집이면 시작하기
#       visit = [[False] * N for _ in range(N)]
#       visit[row][col] = True  # 출발지점
#       dq = deque()
#       dq.append((row, col, 0))  # row,col,이동거리
#       distance = list()
#       while len(dq) != 0:
#         cur = dq.popleft()
#         for dir in dirs:
#           next = (cur[0] + dir[0], cur[1] + dir[1], cur[2] + 1)
#           if 0 <= next[0] < N and 0 <= next[1] < N and visit[next[0]][next[1]] == False:  # 이동가능하고 방문가능한 곳이면
#             if board[next[0]][next[1]] == 1:  # 집이 있는 곳이면
#               visit[next[0]][next[1]] = True
#               distance.append(next)
#             else:  # 치킨집(2) 이나 0 이 있는 곳
#               visit[next[0]][next[1]] = True
#             dq.append(next)
#       distances.append(distance)
#
#
# for distance in distances :
#   distance.sort(key=lambda x : (x[0],x[1]))
# # print2D(distances)
#
# for i in range(1,M+1):
#   for combi in combinations(distances,i) :
#     for i in range(len(combi))

