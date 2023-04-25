import sys

n,k = map(int,sys.stdin.readline().split()) # n : 사건의개수, k : 전후 관계의 개수
distance = [ [float('inf')] * (n+1) for _ in range(n+1)]

for _ in range(k) :
  a,b = map(int,sys.stdin.readline().split())
  distance[a][b] = 1

for i in range(n+1) :
  distance[i][i] = 0 # 자기자신 0으로 초기화

# 플로이드 와샬을 통해서 모든정점까지의 방문 가능성을 확인해야함
for pivot in range(1,n+1) :
  for start in range(1,n+1) :
    for end in range(1,n+1) :
      cost = distance[start][pivot] + distance[pivot][end]
      if cost < distance[start][end] :
        distance[start][end] = cost

s = int(sys.stdin.readline().strip()) # 전후 관계를 알고 싶은 사건의 쌍
targets = list()
for _ in range(s) :
  a,b = map(int, sys.stdin.readline().split())
  targets.append((a,b))


# 출력
  # 앞에 있는 사건이 먼저 일어났으면 -1
  # 뒤에 있는 사건이 먼저 일어났으면 1
  # 유추할 수 없으면 0

# print(distance)
for a,b in targets :
  fisrt = distance[a][b]
  second = distance[b][a]

  if fisrt == float('inf') and second == float('inf') :
    print(0) # 유추 할 수 없는 경우
  elif fisrt < float('inf') :
    print(-1)
  else :
    print(1)
