# DFS ( 깊이 우선탐색 )

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

def dfs(graph,start_node) :
  queue_visited = list()
  stack_will_visit = list()
  # 뽑기 -> 인접노드 방문예정 스택에 추가 -> 방문표시
  cur_node = start_node
  stack_will_visit.extend(graph[cur_node])
  queue_visited.append(cur_node)

  while stack_will_visit :
    cur_node = stack_will_visit.pop()
    print(f"queue_visited : {queue_visited}",end="")
    print(f" stack_will_visit : {stack_will_visit}",end="")
    print(f" cur_node : {cur_node}")
    if cur_node not in queue_visited :
      stack_will_visit.extend(graph[cur_node])
      queue_visited.append(cur_node)
  return queue_visited


if __name__ == '__main__':
  graph = make_graph()
  answer = dfs(graph,"A")
  print(answer)
