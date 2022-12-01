import sys

n = int(sys.stdin.readline())

table = []
for i in range(n) :
  start,end = map(int,sys.stdin.readline().split())
  table.append((start,end))

table.sort(key = lambda x : (x[1],x[0]))
# print(table)

cnt = 0
start = 0

for i in range(len(table)) :
  if start <= table[i][0] :
    cnt+=1
    start = table[i][1]
# print(table)
print(cnt)