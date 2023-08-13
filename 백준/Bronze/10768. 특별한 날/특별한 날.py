import sys

m = int(sys.stdin.readline())
d = int(sys.stdin.readline())


if m < 2 :
  print("Before")
elif m > 2 :
  print("After")
else :
  if d == 18 :
    print("Special")
  elif d < 18 :
    print("Before")
  else :
    print("After")

