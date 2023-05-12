import sys
from itertools import combinations_with_replacement

N,M = map(int,sys.stdin.readline().split())

# 1~N개중 M개를 뽑아야 한다.
arr = [i for i in range(1,N+1)]

for combi in combinations_with_replacement(arr,M):
  print(*combi)