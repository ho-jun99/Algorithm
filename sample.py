import sys

d = dict()
for i in range(35) :
  number,score = map(float,sys.stdin.readline().split())
  d[number] = score

for index,item in sorted(d.values(),reverse=True) :
  print(index, item)