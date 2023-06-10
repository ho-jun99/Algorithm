import sys
from collections import defaultdict

def print2D(arr) :
  for i in arr :
    print(i)
  print()

TC = int(sys.stdin.readline().strip())

def solve() :
  # N 지점의 개수, M 도로의 개수, W 월홀의 개수
  N,M,W = map(int,sys.stdin.readline().split())

  # 플로이드-와샬을 통해서 음의 사이클이 형성되면 종료 후 "YES" 출력하면 됨
  distance = [ [10_001] * (N + 1) for _ in range(N + 1)]

  # 초기화 수행
  for i in range(N+1) :
    distance[i][i] = 0

  # 도로의 정보, 양방향 그래프
  for _ in range(M) :
    S,E,T = map(int,sys.stdin.readline().split())
    if T < distance[S][E] :
      distance[S][E] = T

    if T < distance[E][S] :
      distance[E][S] = T

  # 웜홀의 정보, 단방향 그래프
  for _ in range(W) :
    S, E, T = map(int, sys.stdin.readline().split())
    if -T < distance[S][E] :
      distance[S][E] = -T



  for pivot in range(1,N+1) :
    for start in range(1,N+1) :
      for end in range(1,N+1) :
        cost = distance[start][pivot] + distance[pivot][end]
        if cost < distance[start][end]:
          distance[start][end] = cost
          if start == end and cost < 0 :
            print("YES")
            # print2D(distance)
            return
  # print2D(distance)
  print("NO")

for _ in range(TC) :
  solve()