import sys

N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr= set(arr)
arr = list(arr)
arr.sort()

# 작기자신은 뽑을 수 있는 조합을 하면 된다
# 조합의 개념에서 한발자국 나아가자

result = []
def dfs(idx,cnt) :
  if cnt == M :
    print(*result)
    return

  for i in range( idx, len(arr) ) :
    result.append(arr[i])
    dfs(i,cnt+1)
    result.pop()

dfs(0,0)





