import heapq
import sys

n = int(sys.stdin.readline())

# 파이썬의 힙은 최소힙으로 구현 됨
# 최대힙을 사용하고 싶을때는 - 을 붙여주자


h = []
before = 0
for i in range(n) :
  cur = int(sys.stdin.readline())
  if cur == 0 :
    if len(h) == 0 :
      print(0)
    else :
      popitem = heapq.heappop(h)
      while before == popitem[1] :
        popitem = heapq.heappop(h)
        before = popitem[1]
      print(popitem[1])
  else :
    heapq.heappush(h,(abs(cur),cur))