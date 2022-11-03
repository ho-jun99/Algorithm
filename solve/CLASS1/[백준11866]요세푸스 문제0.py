# 1,2,3,4,5,6,7 :: len == 7
import sys

n,k = map(int,sys.stdin.readline().split())
arr = [i for i in range(1,n+1)]
idx = -1
result = list()
while len(arr) > 0 :
  idx += k
  if ( idx > len(arr)-1) :
    idx %= len(arr)
  result.append(arr.pop(idx))
  idx -=1

print("<",end="")
for i in result :
  if i == result[len(result)-1] :
    print(i,end="")
  else :
    print(i,end=", ")
print(">",end="")

