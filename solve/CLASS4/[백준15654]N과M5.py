import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
ns = list(map(int, sys.stdin.readline().split()))
ns.sort()

for permu in permutations(ns,M) :
  print(*permu)


