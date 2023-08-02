import sys

L,P = map(int,sys.stdin.readline().split())
LP = L*P
arrs = list(map(int,sys.stdin.readline().split()))
for arr in arrs :
  print(arr-LP,end=" ")

