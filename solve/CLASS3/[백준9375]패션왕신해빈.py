import sys
from collections import defaultdict
from itertools import combinations
t = int(sys.stdin.readline())



def solve():
  cnt = 0
  num = int(sys.stdin.readline())
  cloth = defaultdict(int)
  for _ in range(num) :
    _,_type = map(str,sys.stdin.readline().strip().split())
    cloth[_type]+=1

  c = 1
  for value in cloth.values():
    c *= value+1
  print(c-1)



for _ in range(t):
  solve()



