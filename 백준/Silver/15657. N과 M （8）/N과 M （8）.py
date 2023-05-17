'''
  - 중복이 가능하다
  - 범위를 좁혀가며 뽑아야 한다.
'''
import sys

N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
# print(N,M,arr)

def dfs(cur_str,idx,cnt) :
  if cnt == M :
    print(cur_str)
    return

  for i in range(idx, len(arr)) :
    dfs(cur_str + str(arr[i]) + " ", i,cnt+1)

dfs("",0,0)