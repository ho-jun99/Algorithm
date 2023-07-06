import sys


t = int(sys.stdin.readline().strip())
for _ in range(t) :
  a = sys.stdin.readline().strip()
  if 6 <= len(a) <= 9 :
    print("yes")
  else :
    print("no")