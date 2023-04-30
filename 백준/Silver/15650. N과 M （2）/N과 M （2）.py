import sys
from itertools import combinations


N,M = map(int,sys.stdin.readline().split())

# 조합의 문제이다.
for combi in combinations(range(1,N+1), M) :
  print(*combi)
