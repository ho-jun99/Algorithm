import sys


arrs = [1,1,2,2,2,8]
ins = list(map(int,sys.stdin.readline().split()))
results = list()

for i in range(6) :
  results.append(arrs[i]-ins[i])
print(*results)