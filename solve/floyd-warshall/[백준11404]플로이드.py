'''
  - 플로이드-워셜 알고리즘은 모든정점에서부터 모든 정점까지의 최단거리를 구하는 방법
  - DISTANCE를 N*N로 만들고, 행이 시작점, 열이 도착점이 된다.
  - 다익스트라는 그리디 알고리즘 적용, 플로이드 워셜은 다이나믹 프로그래밍이 녹아있음
  - 구해야하는 노드의 갯수가 적으면 플로이-워셜을 사용해도 괜찮
  - 거쳐가는 노드가 반복문의 중심에 있다. - 거쳐가는 노드를 반복문을 하나씩 시작함.
  - 다익스트라는 매번 가장 적은 비용을 가지는 노드를 꺼내서 확인했음
  - O(N^3)
  - 플로이드-워셜 알고리즘
    - DISTANCE테이블을 초기화 시키자 ( 연결된곳은 해당 weight, 갈 수 없느 곳은 INF )
    - for pivot in range(N) :
        for start in range(N) :
          for end in range(N) :
'''

import sys


n = int(sys.stdin.readline().strip()) # 도시의 개수
m = int(sys.stdin.readline().strip()) # 버스의 개수
distance = [ [float('inf')] * (n+1) for _ in range(n+1)]

# 같은 정점간 중복되는 간선이 존재할 수 있음, 그럴 경우 가장 짧은 간선만 사용하면 됨.
for _ in range(m) :
  a,b,c = map(int,sys.stdin.readline().split())
  if c < distance[a][b] :
    distance[a][b] = c

for i in range(n+1) : # 대각행렬 요소(자기 자신)는 0으로 초기화
  distance[i][i] = 0

# 플로이드 워셜을 사용하여 최단거리 업데이트
for pivot in range(1,n+1) :
  for start in range(1,n+1) :
    for end in range(1, n+1 ) :
      cost = distance[start][pivot] + distance[pivot][end]
      if cost < distance[start][end] :
        distance[start][end] = cost

for row in range(1,n+1) :
  for col in range(1,n+1) :
    if distance[row][col] == float('inf') :
      print(0, end=" ")
    else :
      print(distance[row][col], end=" ")
  print()