import sys

stduents = [False] * 31

for _ in range(28) :
  n = int(sys.stdin.readline())
  stduents[n] = True

for i in range(1,31) :
  if stduents[i] == False :
    print(i)