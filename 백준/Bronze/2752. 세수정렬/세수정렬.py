import sys

arrs = list(map(int,sys.stdin.readline().split()))

arrs.sort()
print(*arrs)

