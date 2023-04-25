import queue
import sys

n = int(sys.stdin.readline())

board = [ list(map(int,sys.stdin.readline().strip().split())) for i in range(n) ]
result = [[0 for j in range(n)]for i in range(n)]

# print(board)
# print(result)

q = queue.Queue()

for i in range(n) :
  visit = [False for j in range(n)]
  q.put(i)
  while not q.empty():
    cur = q.get()
    for idx,next in enumerate(board[cur]) :
      if next == 1 and not visit[idx]:
        q.put(idx)
        visit[idx] = True
        result[i][idx] = 1
  # print(visit)

for i in range(len(result)) :
  for j in range(len(result[i])) :
    print(result[i][j],end =" ")
  print()