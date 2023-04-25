'''
  # 플로이드 와샬로 전체 경로 구하고, a->b , b->a의 값으로 사이클여부 판단과 동시에 최단경로 출력이 가능해보이는 문제
'''
import sys

V,E = map(int,sys.stdin.readline().split())
distance = [[float('inf')] * (V+1) for _ in range(V+1)]

for _ in range(E) :
  a,b,c = map(int,sys.stdin.readline().split())
  distance[a][b] = c # 단방향 연결 #같은 도로 여러개 주어지지 않음

for _ in range(V+1) :
  distance[_][_] = 0 # 자기 자신 초기화

for pivot in range(1,V+1) :
  for start in range(1,V+1) :
    for end in range(1,V+1) :
      distance[start][end] = min(distance[start][end], distance[start][pivot] + distance[pivot][end])

mmin = float('inf')
for start in range(1,V+1) :
  for end in range(1,V+1) :
    if start == end :
      continue
    sum = distance[start][end] + distance[end][start]
    mmin = min(sum,mmin)

if mmin == float('inf') :
  print(-1)
else :
  print(mmin)

