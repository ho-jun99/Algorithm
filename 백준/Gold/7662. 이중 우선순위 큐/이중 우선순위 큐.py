'''
  - 정렬을 이용한 풀이방법은 시간초과
    - 정렬 O( k * log N)
  - 힙을 이용해서 풀고 싶다
    - 힙을 두개이용하는 방법 말고 없을까?
    - nlargeset 풀이방법을 이용
  - 중복값이 두번 들어올 수 있다.
    - 이럴경우 dict을 True / False 로 관리하면 관리 할 수 없게 된다.
    - 고유 ID값을 주고 그걸 사용하자.
'''
import sys
from heapq import *
from collections import defaultdict

T = int(sys.stdin.readline().strip())


def solve():
  k = int(sys.stdin.readline().strip())
  minheap = list()
  maxheap = list()
  used = dict()

  for id in range(k):
    operation, num = sys.stdin.readline().split()
    num = int(num)
    if operation == "I":  # 삽입 명령
      heappush(minheap, (num, id))
      heappush(maxheap, (-num, id))
      used[id] = False

    if operation == "D":  # 삭제 명령
      if len(minheap) > 0:
        if num == -1:  # -1 일시 최소값을 뽑아야함
          while len(minheap) > 0:
            poped, id = heappop(minheap)
            if used[id] == False:
              used[id] = True
              break

        if num == 1:  # 1 일시 최대값을 뽑아야함
          while len(maxheap) > 0:
            poped, id = heappop(maxheap)
            if used[id] == False:
              used[id] = True
              break

  # 사용했던 값 제거 ( 양쪽 균형 맞춰 줘야 함 )
  while len(maxheap) > 0:
    if used[maxheap[0][1]] == True:
      heappop(maxheap)
    else:
      break

  while len(minheap) > 0:
    if used[minheap[0][1]] == True:
      heappop(minheap)
    else:
      break
  # print(maxheap,minheap)
  if len(minheap) == 0 and len(maxheap) == 0:
    print("EMPTY")
  else:
    print(maxheap[0][0] * -1, minheap[0][0])


for _ in range(T):
  solve()
