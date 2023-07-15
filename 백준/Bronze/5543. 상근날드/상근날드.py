import sys


bugers = list()
drinks = list()

for i in range(3) :
  b = int(sys.stdin.readline())
  bugers.append(b)

for i in range(2) :
  d = int(sys.stdin.readline())
  drinks.append(d)

mmin = float('inf')

for bug in bugers :
  for dr in drinks :
    mmin = min(bug + dr - 50, mmin)

print(mmin)
