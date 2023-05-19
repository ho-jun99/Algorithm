'''
  - 중복되는 수열을 출력하면 안된다.
  - N개의 자연수 중에서 M개를 고른다.
  - 자기 자신을 두번 뽑지 않는다.
  - 중복을 어떻게 구별할 것인가?
  - 백트래킹으로 swap 시키면 좋을듯
    - 0번인덱스는 항상 선택된걸로하자
'''

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

print(N,M)
print(arr)

def swap(a,b) :
  global arr
  if a==b :
    return
  temp = arr[a]
  arr[a] = b
  arr[b] = temp
  return

def dfs(cur_str, cnt) :
  global arr
  if cnt == M :
    print(cur_str)
    return

  swap(0,cnt)
  for i in range(1,len(arr)) :
    cur_str+= " " + str(arr[i])
    dfs(cur_str,cnt+1)
  swap(cnt,0)

dfs("",0)