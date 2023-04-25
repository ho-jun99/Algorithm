import sys

# BFS로 한칸씩 가면서 탐색
# a==b가 되는 시점에 명령어 출력
from collections import deque, defaultdict


def DSLR(command,num) :
  if command == "D" :
    return (2*num) % 10_000
  elif command == "S" :
    return num-1 if num != 0 else 9_999
  elif command == "L" :
    sNum = str(num)
    sNum = "0" * (4-len(sNum)) + sNum
    sNum = sNum[1:] + sNum[0]
    return int(sNum)
  else: # command == "R"
    sNum = str(num)
    sNum = "0" * (4 - len(sNum)) + sNum
    sNum = sNum[-1] + sNum[:3]
    return int(sNum)

def backward(ddict,cur,start) :
  while True :
    if ddict[cur][0] == start :
      print(ddict[cur][1], end="")
      break
    print(ddict[cur][1],end="")
    cur = ddict[cur][0]


def solve() :
  cur, target = map(int, sys.stdin.readline().strip().split())
  dq = deque()
  dq.append((cur,""))
  commands = ["D","S","L","R"]
  visit = [False for i in range(10_000)]
  # ddict = defaultdict(list)
  # ddict[cur] = (-1,"F")

  while cur != target :
    cur = dq.popleft()
    # print(cur, end="->")
    for command in commands :
      next = DSLR(command, cur[0])
      if not visit[next] :
        dq.append((next,cur[1]+command))
        # ddict[next] = (cur[0],command)
        visit[next] = True
        if next == target:
          print(cur[1]+command)
          return






t = int(sys.stdin.readline())
for _ in range(t) :
  solve()
  print()
