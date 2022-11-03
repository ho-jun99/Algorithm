import math
import sys

t = int(input())

cnt = 0
arr = list(map(int,sys.stdin.readline().strip().split()))
for i in range(t):
  if(arr[i] == 1) :
    continue
  flag = True
  for j in range(2,int(math.sqrt(arr[i]))+1):
    if arr[i] % j == 0 :
      flag = False
      break
  if flag :
    cnt+=1

print(cnt)