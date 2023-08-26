import sys

s = list(sys.stdin.readline().strip())
cnts = [0] * 26
for i in s :
  idx = ord(i) - ord('a')
  cnts[idx] += 1

print(*cnts)



