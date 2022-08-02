"""
  MST (최소신장트리)를 구하는 알고리즘
  탐욕알고리즘과 유사하게 가장 작은 엣지를 순차적으로 선택
  선택된 엣지에 사이클이 존재하는 경우는 pass
  사이클이 생성되는 유무를 확인하기 위해서 union-find 기법을 사용
  union-by-rank 기법을 활용하여 각 트리의 대한 높이를 기억하여 합칠때 사용
  path-compression 를 사용하여 한번 find를 실행한 노드는 다음부터 root노드를 한번에 찾게 해줌
"""

def make_graph():
  graph = {
    "vertices": ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    "edges": [
      (7, 'A', 'B'),
      (5, 'A', 'D'),
      (7, 'B', 'A'),
      (9, 'B', 'D'),
      (8, 'B', 'C'),
      (7, 'B', 'E'),
      (8, 'C', 'B'),
      (5, 'C', 'E'),
      (5, 'D', 'A'),
      (9, 'D', 'B'),
      (7, 'D', 'E'),
      (6, 'D', 'F'),
      (5, 'E', 'C'),
      (7, 'E', 'D'),
      (8, 'E', 'F'),
      (9, 'E', 'G'),
      (7, 'E', 'B'),
      (6, 'F', 'D'),
      (8, 'F', 'E'),
      (11, 'F', 'G'),
      (11, 'G', 'F'),
      (9, 'G', 'E')
      ]
    }
  return graph


parent = dict()
rank = dict()

def make_set(node):
  parent[node] = node
  rank[node] = 0

def find(node):
  if parent[node] == node:
    return node
  root = find(parent[node])
  # path-compression기법을 사용하여 한번 find하면 parent를 root로 바꿔버림
  parent[node] = root
  return root


def union(u,v):
  # root의 랭크를 비교하고 짧은쪽이 긴쪽에 붙어야함
  # rank를 ++ 해주는 경우도 추가해야함
  root_u = find(u)
  root_v = find(v)

  # union-by-rank 기법
  if rank[root_u] > rank[root_v]:
    parent[root_v] = root_u
    rank[root_u] += 1
  else:
    parent[root_u] = root_v
    rank[root_v] += 1

def kruskal(graph):
  mst = list()

  # 부분집합 확인을 위한 set 만들기
  for node in graph["vertices"]:
    make_set(node)

  # 노드들 연결시켜주기
  edges = sorted(graph["edges"])
  cnt = 0
  for edge in edges:
    cnt += 1
    print(cnt)
    weight, vertex_u, vertex_v = edge
    if find(vertex_u) != find(vertex_v):
      mst.append(edge)
      union(vertex_u,vertex_v)

  return mst


if __name__ == '__main__':
  graph = make_graph()
  answer = kruskal(graph)
  print(answer)
