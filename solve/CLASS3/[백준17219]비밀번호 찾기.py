import sys

n,m = map(int,sys.stdin.readline().split())

mydict = dict()
for _ in range(n) :
  web,pwd = map(str,sys.stdin.readline().rstrip().split())
  mydict[web] = pwd

for _ in range(m) :
  print(mydict[sys.stdin.readline().rstrip()])