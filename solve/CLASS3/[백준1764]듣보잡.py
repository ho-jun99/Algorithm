import sys
from collections import defaultdict

n,m = map(int,sys.stdin.readline().rstrip().split())

unlisten = defaultdict(int)
for i in range(n) :
  name = str(sys.stdin.readline().rstrip())
  unlisten[name] += 1

result = []
cnt = 0
for _ in range(m) :
  name = str(sys.stdin.readline().rstrip())
  unlisten[name] +=1
  if unlisten[name] >= 2 :
    cnt +=1
    result.append(name)

result.sort()
print(cnt)
for item in result :
  print(item)
