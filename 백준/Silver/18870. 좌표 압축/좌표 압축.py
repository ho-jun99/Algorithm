import sys
from collections import defaultdict

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

s_arr = list(set(arr)) # 중복 제거
s_arr = sorted(s_arr)

d = dict()
for index,item in enumerate(s_arr) :
  d[item] = index

for i in range(len(arr)) :
  print(d[ arr[i] ],end=" ")






def unsolve() :
  for i in range(n) :
    target = arr[i] # 찾을 원소

    start = 0
    end = len(s_arr)-1
    mid = (start + end) // 2
    while s_arr[mid] != target :
      if target > s_arr[mid] :
        start = mid + 1
        mid = (start + end) // 2
      else :
        end = mid-1
        mid = (start + end) // 2

    print(mid,end=" ")
