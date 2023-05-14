import sys

DIRS = [
  (-1, 0), (0, 1), (1, 0), (0, -1)
  ]


def solve() :
  n = int(sys.stdin.readline().strip())
  stickers = list()
  for row in range(2):
    line = list(map(int, sys.stdin.readline().split()))
    stickers.append(line)

  # 현재 시점에서 대각선으로 한칸전과 두칸전 중 max값이 그 스티커의 최대값
  for i in range(1,n) :
    if i == 1 : # 1일때는 특이 케이스가 된다. 두칸 뒤를 볼 수가 없다.
      stickers[0][i] += stickers[1][i-1]
      stickers[1][i] += stickers[0][i-1]
      continue
    stickers[0][i] = max(stickers[1][i-1],stickers[1][i-2]) + stickers[0][i]
    stickers[1][i] = max(stickers[0][i-1],stickers[0][i-2]) + stickers[1][i]

  # print(stickers)
  print(max(stickers[0][n-1],stickers[1][n-1]))



T = int(sys.stdin.readline().strip())
for _ in range(T):
  solve()