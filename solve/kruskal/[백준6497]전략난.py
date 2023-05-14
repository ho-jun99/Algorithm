import sys
from heapq import *


# m : 집의 수
# n : 길의 수
def find(p,node) :
  if p[node] == node :
    return node
  p[node] = find(p,p[node])
  return p[node]

def union(p,r,nodeA,nodeB) :
  a = find(p,nodeA)
  b = find(p,nodeB)
  if a==b :
    return

  if r[a] < r[b] :
    p[a] = b
  else :
    p[b] = a
    if r[a] == r[b] :
      r[a] +=1


def solve(m,n) :
  edges = list()
  total = 0
  parent = [i for i in range(m+1)]
  rank = [1] * (m+1)

  for _ in range(n) :
    a,b,c = map(int,sys.stdin.readline().split())
    total += c
    heappush(edges,(c,a,b)) # ( cost, a , b )

  cnt = 0
  while True :
    if cnt == m-1 :
      break
    cost, a, b = heappop(edges)

    if find(parent,a) != find(parent,b) :
      union(parent,rank,a,b)
      total -= cost
      cnt+=1

  print(total)


while True :
  m,n = map(int,sys.stdin.readline().split())
  if m == 0 and n == 0 :
    break
  solve(m,n)