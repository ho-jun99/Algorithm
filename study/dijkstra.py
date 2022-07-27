import heapq

CONST_INFINITE = float('inf')

def make_graph():
  graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D' : 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
    }

  return graph

def dijstra(graph, start):
  min_queue = []
  distance_state = {node: CONST_INFINITE for node in graph}

  # 초기화 해주기
  distance_state[start] = 0
  heapq.heappush(min_queue, [distance_state[start], start])
  print(f"__init__ {distance_state}")

  # 힙에서 꺼내오고 비교하기
  while min_queue:
    cur_distance, cur_node = heapq.heappop(min_queue)  # ex) [ 0 : 'A']
    # 이미 최단경로이면 검사할 필요가 없음
    if cur_distance > distance_state[cur_node] :
      continue

    for adjacent_node, weight in graph[cur_node].items() :
      if distance_state[adjacent_node] > cur_distance + weight :
        # update
        update_weight = cur_distance + weight
        distance_state[adjacent_node] = update_weight
        heapq.heappush(min_queue,[update_weight,adjacent_node])
    print(f"distance_state = {distance_state} cur_node : {cur_node}")

  return distance_state


if __name__ == '__main__':
  start = 'A'
  data = make_graph()
  result = dijstra(data,start)

  print(f"\nresult : {result}")