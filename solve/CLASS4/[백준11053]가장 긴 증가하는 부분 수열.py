'''
  - 수열의 크기 N이 최대 1,000이기 때문에 O(N^2)을 이용한 완전탐색을 하더라도
    1,000,000 ( 약 백만 ) 안에 구할 수 있기 때문에 1초안에 구할 수 있을 것으로 보인다.]
  - 잘 건들여보면 O(N)안에 가능할거 같기도하다.
'''
import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
mmax = 1
visit = defaultdict(bool)
for start_index, start in enumerate(arr):
  if visit[start] == True :
    continue
  cnt = 1
  visit[start] = True
  update = start

  for compare_index, compare in enumerate(arr[start_index:]):
    compare_index += start_index
    if compare_index == start_index:
      continue

    if update < compare:
      print(f"{update} -> {compare}, {cnt+1}",end=" || ")
      update = compare
      cnt += 1
  print()
  mmax = max(mmax, cnt)

print(mmax)
