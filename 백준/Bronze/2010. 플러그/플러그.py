import sys

N = int(sys.stdin.readline())

a = 1
arrs = list()
for _ in range(N) :
  i = int(sys.stdin.readline())
  arrs.append(i)

arrs.sort(reverse=True)

for arr in arrs :
  a = a - 1 + arr

print(a)