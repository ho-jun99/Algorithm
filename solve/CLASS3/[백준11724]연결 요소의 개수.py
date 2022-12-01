import sys

n,m = map(int,sys.stdin.readline().split())
l = [i for i in range(n+1)]

# union - find로 찾자

def union(first,second):
  first = find(first)
  second = find(second)

  if first < second :
    l[second] = first
  else :
    l[first] = second

def find(cur):
  if l[cur] == cur :
    return cur
  else :
    return find(l[cur])

# 입력노드에 대한 초기화
for i in range(m):
  first,second = map(int,sys.stdin.readline().split())
  # if l[first] == -1 :
  #   l[first] = first
  # if l[second] == -1 :
  #   l[second] = second
  union(first,second)

cnt = 0
for i in range(1, len(l)) :
  if l[i] == i :
    cnt+=1

print(cnt)