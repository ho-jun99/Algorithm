import sys
from itertools import combinations


N,M = map(int,sys.stdin.readline().split())

# # 조합의 문제이다.
# for combi in combinations(range(1,N+1), M) :
#   print(*combi)


# 백트래킹으로 풀기
def dfs(arr,index) :
  if len(arr) == M :
    print(*arr)
    return

  for i in range(index,N+1) :
    arr.append(i)
    dfs(arr, i+1 )
    arr.pop()

dfs([],1)