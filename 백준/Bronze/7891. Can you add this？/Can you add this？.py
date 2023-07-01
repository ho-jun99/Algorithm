import sys

s = int(sys.stdin.readline().strip())
for _ in range(s) :
  a,b = map(int,sys.stdin.readline().split())
  print(a+b)
