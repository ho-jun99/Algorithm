import sys
from collections import deque
from collections import defaultdict



def solve(n,m) :
  ddict = defaultdict(list)
  for _ in range(m) :
    a,b = map(int,sys.stdin.readline().split())
    ddict[a].append(b)
    ddict[b].append(a)

  # 1. 트리의 개수를 셀 수 있어야 한다.
  # 2. 트리가 아닌지( 사이클을 가지는지 확인해야 한다)
  # 2-1. 사이클을 구별하기 위해서, 트리를 양방향으로 만들어서 BFS를 돌리고, visit조건으로 판단한다.
  # 2-2. 양방향으로 만들면 visit에서 방금전에 넘어온건 무조건 체킹 되기 때문에, 이전 부모노드를 넘겨주고 해당건은 패스 시키도록 한다.

  T = 0 # 트리의 개수
  visit = [False] * (n+1)

  for i in range(1,n+1) : # 1부터 n까지의 노드(vertex)를 대상으로 삼는다.
    if visit[i] == False : # 방문했던 곳이 아니라면
      isCycle = False
      dq = deque()
      dq.append((i,-1)) # 시작 노드 넣어주기
      visit[i] = True # 시작 노드 방문처리 해주기

      if len(ddict[i]) == 0 : # 혼자 있는 노드
        # print(f"len : {len(ddict[i])}")
        T+=1
        continue

      while len(dq) != 0 :
        cur = dq.popleft() # bfs 활용
        # print(f"{i} : {cur}")

        for next in ddict[cur[0]] : # 다음 방문예정지
          if next == cur[1] :
            continue # 여기가 특수조건, 트리를 양방향으로 표현했기 때문에, visit를 처리하기 위해서

          if visit[next] == True : # 사이클이 생겨버린 것임
            isCycle = True

          if not isCycle and visit[next] == False :
            dq.append((next,cur[0]))
            # print(f"{cur} -> {next}")
            visit[next] = True

      if not isCycle :
        T +=1

  return T



case = 1
while True :
  n,m = map(int,sys.stdin.readline().split())
  if n == 0 and m == 0 :
    break
  result = solve(n,m)

  if result == 0 :
    print(f"Case {case}: No trees.")
  elif result == 1 :
    print(f"Case {case}: There is one tree.")
  else :
    print(f"Case {case}: A forest of {result} trees.")


  case+=1
