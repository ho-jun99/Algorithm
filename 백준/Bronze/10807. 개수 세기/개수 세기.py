import sys

a = int(sys.stdin.readline())
arrs = map(int,sys.stdin.readline().split())
target = int(sys.stdin.readline())

cnt = 0

for arr in arrs :
  if arr == target :
    cnt +=1

print(cnt)