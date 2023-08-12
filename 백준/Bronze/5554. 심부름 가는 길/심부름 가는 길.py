import sys

time = 0
for _ in range(4) :
  time += int(sys.stdin.readline())



m = time // 60
s = time % 60

print(m)
print(s)