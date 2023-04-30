import sys
from itertools import permutations

N,M = map(int,sys.stdin.readline().split())
targets = [i for i in range(1,N+1)]
# print(targets)

# 중복없이 M개를 고른 수열
  # 조합을 사용한다.
for permu in permutations(targets,M) :
  print(*permu)



