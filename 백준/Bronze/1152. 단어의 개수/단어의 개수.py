import sys

arrs = sys.stdin.readline().strip().split(" ")
# print(arrs)

if len(arrs) == 1 and arrs[0] == '':
  print(0)
else :
  print(len(arrs))