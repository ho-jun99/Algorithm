import sys


t = int(sys.stdin.readline())

for _ in range(t) :
  arrs = map(int,sys.stdin.readline().split())
  candidates = list()
  sum = 0
  mmin = float('inf')
  for arr in arrs :
    if arr % 2 == 0 :
      # 짝수이면
      sum += arr
      mmin = min(mmin,arr)

  print(sum, mmin)