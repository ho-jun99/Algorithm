import math
import sys

n, m = map(int,sys.stdin.readline().split())

for num in range(n,m+1) :
  if num == 1 :
    continue
  if num == 2 :
    print(2)
    continue
  flag = True
  for i in range(2,int(math.sqrt(num))+1) :
    if num % i == 0 :
      flag = False
      break
  if flag :
    print(num)