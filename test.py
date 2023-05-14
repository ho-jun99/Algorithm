from collections import deque
import heapq


def solution(n):
  answer = 0
  # dq = deque()
  result = set()
  # dq.append(4)
  # dq.append(13)
  hq = list()
  heapq.heappush(hq, 4)
  heapq.heappush(hq, 13)
  # result.add(4)
  # result.add(13)

  nums = ["4", "13"]
  cnt = 0
  while True:
    if n + 1 < len(hq):
      break
    cur = heapq.heappop(hq)
    result.add(cur)
    for num in nums:
      heapq.heappush(hq, int(str(cur) + num))
      heapq.heappush(hq, int(num + str(cur)))

    cnt += 1

  result = list(result)
  result.sort()

  print(result)
  # return result[n - 1]

solution(10)