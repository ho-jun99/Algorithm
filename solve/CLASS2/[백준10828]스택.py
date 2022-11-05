import sys

n = int(input())

stack = list()
for i in range(n):
  com = list(map(str,sys.stdin.readline().rstrip().split()))
  if com[0] == "push" :
    stack.append(int(com[1]))
  elif com[0] == "top" :
    if len(stack) > 0 :
      print(stack[len(stack)-1])
    else:
      print(-1)
  elif com[0] == "pop" :
    if len(stack) > 0 :
      print(stack.pop())
    else :
      print(-1)
  elif com[0] == "size" :
    print(len(stack))
  elif com[0] == "empty" :
    if len(stack) == 0 :
      print(1)
    else :
      print(0)
