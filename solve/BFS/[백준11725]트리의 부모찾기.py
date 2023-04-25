import sys
from collections import deque
from collections import defaultdict

N = int(sys.stdin.readline().strip())

ddict = defaultdict(list)
result = [-1] * (N+1)

for i in range(N-1) :
  a,b = map(int,sys.stdin.readline().strip().split())
  ddict[a].append(b)
  ddict[b].append(a)

dq = deque()
dq.append(1)
result[1] = 1

while len(dq) != 0 :
  cur = dq.popleft()

  for next in ddict[cur] :
    # print(f"cur : {cur} , next : {next}")
    if result[next] == -1 :
      result[next] = cur
      dq.append(next)


for i in range(2,N+1) :
  print(result[i])




