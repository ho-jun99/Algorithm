import sys

n = int(sys.stdin.readline().strip())

myset = set()
for i in range(n):
  com = sys.stdin.readline().split()
  if com[0] == "add":
    myset.add(int(com[1]))

  elif com[0] == "remove":
    myset.discard(int(com[1]))

  elif com[0] == "check":
    if int(com[1]) in myset:
      print(1)
    else :
      print(0)

  elif com[0] == "toggle":
    if int(com[1]) in myset:
      myset.remove(int(com[1]))
    else :
      myset.add(int(com[1]))
  elif com[0] == "all" :
    myset = set([i for i in range(1,21)])

  elif com[0] == "empty":
    myset.clear()


