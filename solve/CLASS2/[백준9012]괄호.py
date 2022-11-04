import sys

n = int(input())

def solve():
  str = sys.stdin.readline().strip()
  stack = list()
  for i in range(len(str)):
    if str[i] == "(" :
      stack.append(str[i])
    else :
      if (len(stack) == 0) :
        print("NO")
        return
      else : stack.pop()

  if len(stack) == 0 : print("YES")
  else : print("NO")

for i in range(n) :
  solve()