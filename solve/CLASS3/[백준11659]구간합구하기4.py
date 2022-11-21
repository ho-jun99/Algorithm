import sys

n,m = map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().strip().split()))
data.insert(0,-1)
# print(data)
prefixsum = [0]*int((n+1))

sum = 0
for i in range(1,n+1) :
  prefixsum[i] = prefixsum[i-1]+data[i]
# print(prefixsum)



for _ in range(m) :
  start,end = map(int,sys.stdin.readline().split())
  print(prefixsum[end]-prefixsum[start-1])
