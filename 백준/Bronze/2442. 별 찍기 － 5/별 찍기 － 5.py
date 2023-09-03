import sys


n = int(sys.stdin.readline().strip())
blank = n-1
for i in range(1,2*n+1,2) :
  print(" "* blank,end="")
  print("*"*i)
  blank-=1


