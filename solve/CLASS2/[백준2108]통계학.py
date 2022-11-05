import math
import sys
from collections import defaultdict

n = int(sys.stdin.readline())

mydic = defaultdict(int)
arr = list()

sum = 0
for i in range(n) :
  num = int(sys.stdin.readline())
  sum += num
  mydic[num] += 1
  arr.append(num)

arr.sort()
# 평균
print(round(sum / len(arr)))

# 중앙값
print(arr[len(arr)//2])

# 최빈값
max_value = max(mydic.values())
temp = list()
for key in sorted(mydic.keys()) :
  if mydic[key] == max_value :
    temp.append(key)
  if len(temp) == 2 :
    break

if len(temp) > 1 :
  print(temp[1])
else :
  print(temp[0])

# 범위
print(arr[len(arr)-1]-arr[0])
