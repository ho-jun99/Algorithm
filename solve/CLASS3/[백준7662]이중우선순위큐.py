import queue
import sys





# D 1 -> Q에서 최댓값을 삭제하는 연산,
# D -1 -> Q에서 최솟값을 삭제하는 연산 , 둘일 경우 하나만 삭제 됨
# I n -> 큐에 n을 삽입, 동일한 정수가 삽입 될 수 있음
from collections import deque


def solve() :
  k = int(sys.stdin.readline().strip())  # 연산의 개수
  pque = queue.PriorityQueue()
  for i in range(k) :
    command, num = sys.stdin.readline().strip().split()
    num = int(num)
    if command == "I" :
      pque.put(num)
    else :
      pass





t = int(sys.stdin.readline().strip())  # 연산의 개수
for i in range(t) :
  solve()
