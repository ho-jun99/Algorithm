import copy
import sys
from collections import deque

A, B, C = map(int, sys.stdin.readline().split())
max_size = (A, B, C)
result = set()

# visit를 어떻게 처리할 것인가 ?
## 병이 똑같은 상태가 된다면 visit로 처리하는게 맞을듯 하다.
## 3차원 배열을 쓰는건 너무 메모리 낭비가 클까?

# 물을 붓는 행위 ( next ) 를 어떻게 할 것인가
# 종료조건은 무엇이 되는가 ?

visit = [[[False] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)]
# print(sys.getsizeof(visit)) # 사용하는 메모리 크기를 알아보기 위해서

dq = deque()
dq.append((0, 0, C))  # 마지막은 몇번째 순서인지 알기 위해서 사용
visit[0][0][C] = True  # 방문처리를 해준다
result.add(C)

while len(dq) != 0:
  cur = dq.popleft()

  # 0, 0, 10
  for index, size in enumerate(cur):
    if size == 0:
      continue

    for other in range(3):
      if other == index:  # 자신을 제외한 다른 물통을 선택
        continue

      # index =2 , [other 0, other 1]

      # 다른 물통이 가득찰때까지 물을 붓는 조건
      useage = max_size[other] - cur[other]
      next = copy.deepcopy(list(cur))  # tuple을 쓰면 변경이 안된다.
      next[other] += useage
      next[index] -= useage
      # ------------------------------

      # 물통의 용량이 0일될때까지 붓는 조건
      using_able = cur[index]
      next2 = copy.deepcopy(list(cur))  # tuple을 쓰면 변경이 안된다.
      next2[index] = 0
      next2[other] = cur[other] + using_able
      # ------------------------------

      if 0 <= next[0] <= max_size[0] and 0 <= next[1] <= max_size[1] and 0 <= next[2] <= max_size[2]:
        if visit[next[0]][next[1]][next[2]] == False:
          dq.append(next)
          visit[next[0]][next[1]][next[2]] = True
          if next[0] == 0 :
            result.add(next[2])
          # print(f"{cur} -> {next}")

      if 0 <= next2[0] <= max_size[0] and 0 <= next2[1] <= max_size[1] and 0 <= next2[2] <= max_size[2]:
        if visit[next2[0]][next2[1]][next2[2]] == False:
          dq.append(next2)
          visit[next2[0]][next2[1]][next2[2]] = True
          if next2[0] == 0:
            result.add(next2[2])
          # print(f"{cur} -> {next2}")

result = list(result)
result.sort()
print(*result)