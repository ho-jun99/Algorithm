import sys

t = int(input())


deque = list()
for _ in range(t) :
  com = list(map(str, sys.stdin.readline().rstrip().split()))
  if com[0] == "push_front" :
    deque.insert(0,int(com[1]))

  elif com[0] == "push_back" :
    deque.append(int(com[1]))

  elif com[0] == "pop_front" :
    if len(deque) > 0 :
      print(deque.pop(0))
    else :
      print(-1)

  elif com[0] == "pop_back" :
    if len(deque) > 0 :
      print(deque.pop(len(deque)-1))
    else :
      print(-1)
  elif com[0] == "size" :
    print(len(deque))

  elif com[0] == "empty" :
    if len(deque) > 0 :
      print(0)
    else:
      print(1)

  elif com[0] == "front" :
    if len(deque) > 0:
      print(deque[0])
    else:
      print(-1)

  elif com[0] == "back" :
    if len(deque) > 0:
      print(deque[len(deque) - 1])
    else:
      print(-1)