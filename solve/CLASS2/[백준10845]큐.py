import sys

t = int(input())


q = list()
for _ in range(t) :
  com = list(map(str, sys.stdin.readline().rstrip().split()))
  if com[0] == "push" :
    q.append(int(com[1]))
  elif com[0] == "pop" :
    if len(q) > 0 :
      print(q.pop(0))
    else:
      print(-1)
  elif com[0] == "size" :
    print(len(q))
  elif com[0] == "empty" :
    if len(q) > 0 :
      print(0)
    else:
      print(1)
  elif com[0] == "front" :
    if len(q) > 0:
      print(q[0])
    else:
      print(-1)
  elif com[0] == "back" :
    if len(q) > 0:
      print(q[len(q)-1])
    else:
      print(-1)