"""
  Prim알고리즘을 이용하여 MST(최소신장트리)구하기
  크루스칼 알고리즘은 모든 엣지의 정보를 이미 알고 있는 상태에서 출발하지만,
  프림알고리즘은 주어진 시작노드에서부터 하나씩 추가해나가면서 구현함
"""
from collections import defaultdict
import heapq

def make_edges():
  edges = [
    (7, 'A', 'B'),(5, 'A', 'D'),
    (8, 'B', 'C'),(9, 'B', 'D'),(7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'),(6, 'D', 'F'),
    (8, 'E', 'F'),(9, 'E', 'G'),
    (11, 'F', 'G'),
    ]
  return edges

def prim(start_node,edges):
  mst = list()
  adjacent_edges = defaultdict(list)
  selected_vertex = set()

  # 노드별 엣지 초기화 해주기 ( u->v )
  for weight,node_u,node_v in edges:
    adjacent_edges[node_u].append((weight,node_u,node_v))
    adjacent_edges[node_v].append((weight,node_v,node_u))

  # 시작 노드 넣어주기
  selected_vertex.add(start_node)
  candidate_edges = adjacent_edges[start_node]
  heapq.heapify(candidate_edges)

  # 검사 및 선택
  while candidate_edges:
    cur_weight,cur_u,cur_v = heapq.heappop(candidate_edges)
    if cur_v not in selected_vertex:
      selected_vertex.add(cur_v)
      mst.append((cur_weight,cur_u,cur_v))

      for edge in adjacent_edges[cur_v]:
        if edge[2] not in selected_vertex:
          heapq.heappush(candidate_edges,edge)

  return mst

if __name__ == '__main__':
    my_edges = make_edges()
    answer = prim('A',my_edges)
    print(answer)
