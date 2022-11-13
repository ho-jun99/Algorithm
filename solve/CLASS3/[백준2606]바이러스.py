import sys
from collections import defaultdict

c = int(sys.stdin.readline())
t = int(sys.stdin.readline())

l = [i for i in range(0,c+1)]
# print(l)

# 해당 원소의 루트 노드를 찾음
def find(a) :
  if l[a] == a : return a # 자기 자신이 루트인 경우
  l[a] = find(l[a])
  return l[a] # 재귀적으로 루트노드를 찾게 함

# 루트노드에 합쳐줌
def union(a,b):
  a = find(a)
  b = find(b)

  if a < b :
    l[b] = a
  else:
    l[a] = b

for _ in range(t) :
  a,b = map(int,sys.stdin.readline().split())
  union(a,b)

cnt = 0
for i in range(2,c+1) :
  if find(i) == 1 :
    cnt+=1
# print(l)
print(cnt)







