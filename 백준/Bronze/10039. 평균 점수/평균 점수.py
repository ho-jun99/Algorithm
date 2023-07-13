import sys

sum = 0
for _ in range(5) :
  a = int(sys.stdin.readline())
  if a < 40 : 
    sum += 40
  else :
    sum += a

print(sum//5)