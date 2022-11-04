import sys

t = int(input())

list = list()
for i in range(t) :
  m = tuple(map(int,sys.stdin.readline().split()))
  list.append(m)

list.sort(key= lambda x : (x[1],x[0]))

for i in range(len(list)):
  print(f"{list[i][0]} {list[i][1]}")