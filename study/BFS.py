# bfs ( 넓이 우선 탐색 )

def make_graph() :
  graph = dict()
  graph["A"] = ["B","C","D"]
  graph["B"] = ["A","E"]
  graph["C"] = ["A"]
  graph["D"] = ["A","F","G"]
  graph["E"] = ["B","H"]
  graph["F"] = ["D","I","J"]
  graph["G"] = ["D"]
  graph["H"] = ["E"]
  graph["I"] = ["F"]
  graph["J"] = ["F"]
  print(f"make OK {graph}")
  return graph

def bfs(graph,start_node) :
  # 큐 초기화
  queue_visited = list()
  queue_will_visit = list()

  # 시작노드
  cur_node = start_node
  # 시작노드와 연결된 노드 큐에 추가
  queue_will_visit.extend(graph[cur_node])
  # 방문 완료
  queue_visited.append(cur_node)

  while queue_will_visit :
    print(f"queue_visited : {queue_visited}",end="")
    print(f" queue_will_visit : {queue_will_visit}",end="")
    print(f" cur_node : {cur_node}")

    # 방문해야할 노드 하나 뽑음
    cur_node = queue_will_visit.pop(0)
    # 방문한 기록이 없다면
    if cur_node not in queue_visited :
      # 방문해야하는 노드들 기록
      queue_will_visit.extend(graph[cur_node])
      # 방문 완료
      queue_visited.append(cur_node)

  return queue_visited


if __name__ == '__main__':
  graph = make_graph()
  answer = bfs(graph,"A")
  print(answer)
