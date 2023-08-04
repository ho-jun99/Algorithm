import sys

mmin = float('inf')
sum = 0
for _ in range(7) :
  num = int(sys.stdin.readline())
  if num % 2 == 1 :
    mmin = min(mmin,num)
    sum += num

if mmin == float('inf') :
  print(-1)
else :
  print(sum)
  print(mmin)