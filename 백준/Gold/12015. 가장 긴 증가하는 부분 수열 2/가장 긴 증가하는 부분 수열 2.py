import sys
import bisect
N = int(sys.stdin.readline())
arrs = list(map(int,sys.stdin.readline().split()))
infArrs = [float('inf')] * N

for i in range(N) :
  idx = bisect.bisect_left(infArrs,arrs[i])
  infArrs[idx] = arrs[i]

result = list()
for infArr in infArrs :
  if infArr != float('inf') :
    result.append(infArr)

print(len(result))