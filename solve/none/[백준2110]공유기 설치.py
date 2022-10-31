import sys

house = []
def solve():
  N,C = map(int,sys.stdin.readline().strip().split())
  for _ in range(N):
    house.append(int(sys.stdin.readline().strip()))

  house.sort()
  print(house)

  start = 0
  end = len(house)-1
  cnt = 0
  min

  # 짝수개 0,1,2,3,4,5 : mid== 0+5 = 5 / 2 = 2.5 == 2
  # 혹수개 0,1,2,3,4,5,6 : mid == 0+6 = 6 / 2 == 3
  while cnt != C :



if __name__ == '__main__':
    solve()
