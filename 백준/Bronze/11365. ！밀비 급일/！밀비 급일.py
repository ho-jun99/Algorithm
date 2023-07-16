import sys


while True :
  s = sys.stdin.readline().strip()
  if s == "END" :
    break
  arrs = list(s)
  arrs.reverse()
  for arr in arrs :
    print(arr, end="")
  print()