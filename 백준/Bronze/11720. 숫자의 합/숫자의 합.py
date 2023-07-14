import sys

a = int(sys.stdin.readline())
arrs = list(sys.stdin.readline().strip())
sum = 0
for n in arrs :
  sum += int(n)
print(sum)

