import sys

def find(parent,node):
  # 재귀함수의 종료조건
  # 부모를 찾으면..!
  if parent[node] == node:
    return node
  up = parent[node]
  root = find(parent,up)

  # 다음번에 해당 노드를 방문하여 root를 한번에 찾을 수 있도록
  parent[node] = root

  return root

def union(parent,weight,a,b):
  # 같은 네트워크내에 존재하는지 확인하기 위해서 최소신장트리(root)를 비교해야함
  root_a = find(parent,a)
  root_b = find(parent,b)

  # 같지 않다면 b노드를 a의 root에 연결시켜줌
  if root_a != root_b:
    parent[root_b] = root_a
    # 최소신장트리간 연결될때 해당 트리의 root의 총 weight를 더해줌
    weight[root_a] += weight[root_b]


def solve(n):
  for _ in range(n):
    F = int(input())
    parent = dict()
    weight = dict()

    for _ in range(F):
      node_a,node_b = sys.stdin.readline().strip().split()
      # 노드 초기화
      if node_a not in parent:
        parent[node_a] = node_a
        weight[node_a] = 1
      if node_b not in parent:
        parent[node_b] = node_b
        weight[node_b] = 1

      # a<-b의 엣지 형성
      union(parent,weight,node_a,node_b)
      # 출력은 연결된 놈의 root의 weight를 보여줘야함
      print(weight[find(parent,node_a)])

if __name__ == '__main__':
    n = int(input())
    solve(n)