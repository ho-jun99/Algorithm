import sys
import queue
from collections import defaultdict


# n정점의개수, m간선의 개수, v탐색시작정점


def dfs(n,s,start):
  mstack = list()
  visit = [False] * int(n+1)
  mstack.append(start)

  while len(mstack) > 0 :
    cur_node = mstack.pop()
    for next_node in sorted(s[cur_node],reverse=True) :
      if not visit[next_node] :
        mstack.append(next_node)
    if visit[cur_node] :
      continue
    else :
      print(cur_node, end=" ")
      visit[cur_node] = True

def bfs(n,s,start):
  q = queue.Queue()
  visit = [False] * int(n+1)
  q.put(start)
  while not q.empty() :
    cur_node = q.get()
    s[cur_node].sort()
    for next_node in s[cur_node] :
      if not visit[next_node] :
        q.put(next_node)

    if visit[cur_node] == True :
      continue
    visit[cur_node] = True
    print(cur_node, end=" ")


n,m,v = map(int,sys.stdin.readline().split())
s = defaultdict(list)
for _ in range(m) :
  n1,n2 = map(int,sys.stdin.readline().split())
  s[n1].append(n2)
  s[n2].append(n1)

dfs(n,s,v)
print()
bfs(n,s,v)
