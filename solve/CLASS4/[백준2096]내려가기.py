'''
  - 메모리 제한이 4MB이다.
    - 아마 BFS를 이용한 풀이는 메모리 제한에 걸릴거 같다.
  - 그리디를 이용한 풀이를 사용해야 하는 것인가?
    - 그리디를 이용한 풀이가 최적해를 구한다는 보장은 없다.
  - DP를 써야하는거 같은데..
    - 슬라이딩 윈도우?
'''
import sys

N = int(sys.stdin.readline().strip())
board = list()
visit = [[False] * N for _ in range(N)]

for _ in range(N):
  line = list(map(int, sys.stdin.readline().split()))
  board.append(line)


