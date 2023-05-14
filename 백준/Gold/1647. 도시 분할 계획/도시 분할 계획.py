'''
  - 마을을 두개로 분리해야한다.
    - 마을을 두개로 분리할때, MST로 만들고 간선 하나를 떼버리면 마을이 두개로 분리된다.
    - 그렇다면 가장 큰 값을 가진 간선을 떼버리면 되지 않을까
'''
import sys
from heapq import *

N, M = map(int, sys.stdin.readline().split())  # N : 집의 개수, M : 길의 개수
edges = list()

parent = [i for i in range(N + 1)]
rank = [1] * (N + 1)


def find(node):
  if parent[node] == node:
    return node
  parent[node] = find(parent[node])
  return parent[node]


def union(nodeA, nodeB):
  a = find(nodeA)
  b = find(nodeB)

  if a == b:  # 아무것도 할 필요가 없다.
    return

  if rank[a] < rank[b]:
    parent[a] = b
  else:
    parent[b] = a
    if rank[a] == rank[b]:  # 같으면
      rank[a] += 1


for _ in range(M):
  a, b, c = map(int, sys.stdin.readline().split())
  # print(c,a,b)
  heappush(edges,(c, a, b))

# 크루스칼을 통해서 MST를 구한다
cnt = 0
result = 0
mmax = 0
while True:
  if cnt == N - 1 :  # 종료조건
    break
  cur = heappop(edges)  # ( weight, a , b  )
  # print(cur)
  if find(cur[1]) != find(cur[2]):  # 같은 집합이 아니라면
    # print("👆👆pop👆👆")
    union(cur[1], cur[2])
    mmax = max(mmax,cur[0])
    result += cur[0]
    cnt += 1

# print(parent)
print(result-mmax)
