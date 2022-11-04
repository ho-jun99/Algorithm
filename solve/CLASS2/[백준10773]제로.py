import sys

n = int(input())

stack = list()
sum = 0
for i in range(n):
  num = int(sys.stdin.readline())
  if num == 0 :
    sum -= stack.pop()
  else:
    stack.append(num)
    sum += num

print(sum)

