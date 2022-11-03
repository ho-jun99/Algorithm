import sys
from itertools import combinations, permutations,product

n, k = map(int, sys.stdin.readline().split())

combi = combinations(range(n), k)
combi = product(range(n), k)
print(len(list(combi)))