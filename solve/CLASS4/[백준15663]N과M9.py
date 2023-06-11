'''
  - 중복되는 수열을 출력하면 안된다.
  - N개의 자연수 중에서 M개를 고른다.
  - 자기 자신을 두번 뽑지 않는다.
'''

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()


used = [False] * (N+1)
result = set()

def dfs(chosen, used) :
  if len(chosen) == M :
    result.add(tuple(chosen))
    return

  for i in range(len(arr)) :
    if used[i] :
      continue
    chosen.append(arr[i])
    used[i] = True
    dfs(chosen,used)
    used[i] = False
    chosen.pop()

dfs([],used)
result = list(result)
result.sort()

for item in result :
  print(*item)