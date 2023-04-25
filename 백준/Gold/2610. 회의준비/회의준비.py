'''
  - 플로이드-와샬을 이용해서 다른 노드까지의 방문의 합이 최소인 노드를 대표로노드로 선정한다
    - 근데 같은 집단(위원회)인건 어떻게 구별해야하나?
    - 보통 집단을 찾는건 BFS를 활용하기는 하는데.. OR UNION - FIND
    - 일단 못가는 곳은 INF로 표현 되긴 함
    - 유니온 파인드로 구분하는 전처리 과정을 거치자
      https://eun-jeong.tistory.com/15
'''

import sys
from collections import defaultdict

N = int(sys.stdin.readline()) # 참석 하는 사람의 수
M = int(sys.stdin.readline()) # 서로 알고 있는 사람

distance = [[float('inf')] * (N+1) for _ in range(N+1)]

# union-find로 집합여부를 먼저 판단하자
parent = [i for i in range(N+1)]
rank = [1 for i in range(N+1)]

def find(node) :
  if parent[node] == node :
    return node
  parent[node] = find(parent[node])
  return parent[node]

def union(nodeA, nodeB) :
  a = find(nodeA)
  b = find(nodeB)

  # 항상 높이가 더 낮은 트리를 높이가 더 높은 트리 밑에 넣는다.
  if rank[a] < rank[b] :
    parent[a] = b
  else :
    parent[b] = a
    if rank[a] == rank[b] : # Rank가 같다면, b를 a에 붙였기 때문에 a의 랭크를 1 올려줘야함 ( 루트 )
      rank[a] += 1



for _ in range(M) :
  a,b = map(int,sys.stdin.readline().split())
  # 양방향 관계
  distance[a][b] = 1
  distance[b][a] = 1
  union(a,b) # 유니온 파인드 수행



for i in range(N+1) :
  distance[i][i] = 0 # 시작 노드 초기화


for pivot in range(1, N+1) :
  for start in range(1, N+1) :
    for end in range(1, N+1) :
      distance[start][end] = min(distance[start][pivot] + distance[pivot][end], distance[start][end])





result = defaultdict(lambda : (float('inf'), -1)) # 초기값을 inf로 하기 위해서
for index,item in enumerate(parent[1:]) :
  index += 1
  item = find(item)
  # 최대값 찾기
  # 찾은 최대값과 현재 캐싱된 값 비교
  # 찾은 최대값이 더 작다면 업데이트

  mmax = -1
  for i in distance[index][1:] :
    if i == float('inf') :
      continue
    if mmax < i :
      mmax = i # 최대값 찾기

  if mmax < result[item][0] :
    result[item] = (mmax, index)


# print(parent)
# print(result)
# for i in range(1,N+1) :
#   print(*distance[i][1:])
# print()

print(len(result))
for item in sorted(list(result.values()), key = lambda x : x[1] ) :
  print(item[1])