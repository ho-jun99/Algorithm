import sys

def solve(stack, str) :
  for i in range(len(str)):
    if str[i] == "(" or str[i] == "[" :
      stack.append(str[i])
    elif str[i] == ")" or str[i] == "]" :
      if len(stack) == 0 :
        print("no")
        return
      else :
        if str[i] == ")" :
          if stack.pop() != "(" :
            print("no")
            return
        if str[i] == "]" :
          if stack.pop() != "[" :
            print("no")
            return

  if len(stack) == 0 :
    print("yes")
  else:
    print("no")

while True :
  s = str(sys.stdin.readline().rstrip())
  if s == ".":
    break
  stack = list()
  solve(stack,s)
  stack.clear()

