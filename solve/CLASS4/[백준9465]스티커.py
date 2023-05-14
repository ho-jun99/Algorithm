import sys

DIRS = [
  (-1, 0), (0, 1), (1, 0), (0, -1)
  ]


def solve() :
  n = int(sys.stdin.readline().strip())
  stickers = list()
  for row in range(2):
    line = list(map(int, sys.stdin.readline().split()))
    stickers.append(line)

  # 현재 시점에서 대각선으로 한칸전과 두칸전 중 max값이 그 스티커의 최대값
  for i in range(1,n) :
    if i == 1 : # 1일때는 특이 케이스가 된다. 두칸 뒤를 볼 수가 없다.
      stickers[0][i] += stickers[1][i-1]
      stickers[1][i] += stickers[0][i-1]
      continue
    stickers[0][i] = max(stickers[1][i-1],stickers[1][i-2]) + stickers[0][i]
    stickers[1][i] = max(stickers[0][i-1],stickers[0][i-2]) + stickers[1][i]

  # print(stickers)
  print(max(stickers[0][n-1],stickers[1][n-1]))



T = int(sys.stdin.readline().strip())
for _ in range(T):
  solve()


# # --- 그리디를 이용했던 풀이는 역시나 틀렸다 --- #
# def solve():
#   n = int(sys.stdin.readline().strip())
#   stickers = list()
#   max_heap = list()
#   visit = [[False] * n for _ in range(2)]
#   for row in range(2):
#     line = list(map(int, sys.stdin.readline().split()))
#     stickers.append(line)
#     for col, cost in enumerate(line):
#       node = (cost * -1, row, col)  # cost, row, col # -1을 곱해줌으로써 max_heap의 형태로 만든다.
#       heappush(max_heap, node)
#   result = 0
#
#   visit_cnt = 0
#   while len(max_heap) != 0:
#     cost, row, col = heappop(max_heap)  # ( cost, row, col )
#     cost *= -1  # cost에 -1을 곱해서 원복을 해야한다
#     if visit[row][col] == False:  # 사용했던 곳이 아니면
#       visit[row][col] = True  # 방문처리
#       visit_cnt += 1
#       result += stickers[row][col]
#       # print(row, col)
#
#       for dir in DIRS:  # 4방향 방문처리
#         next_row = row + dir[0];
#         next_col = col + dir[1]
#         if 0 <= next_row <= 1 and 0 <= next_col < n and visit[next_row][next_col] == False:  # 범위 안이라면
#           visit[next_row][next_col] = True  # 방문처리를 완료한다.
#           visit_cnt += 1
#
#     if visit_cnt == 2 * n:  # 모든 곳 방문했기에 종료
#       # print(f"visit : {visit}")
#       # print(f"visit_cnt : {visit_cnt}")
#       # print(f"2*n : {2 * n}")
#       break
#   print(result)