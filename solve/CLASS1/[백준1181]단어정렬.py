import sys

n = int(input())

s = set()
for i in range(n):
  s.add(sys.stdin.readline().strip())

s = list(s)
s.sort(key=lambda x:(len(x),x))
for i in range(len(s)):
  print(s[i])