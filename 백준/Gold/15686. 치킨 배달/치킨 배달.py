import sys
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