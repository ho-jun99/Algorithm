'''
  - 집을 조건에 맞게 칠할때, 최소 비용을 구해라
  - 중점을 두는 것을, 현재 값에 중점을 두고 과거를 봐야한다.
'''
import sys

N = int(sys.stdin.readline().strip())
arr = list()
# RGB로 칠하는 비용
for _ in range(N):
  line = list(map(int, sys.stdin.readline().split()))
  arr.append(line)

for house in range(1,N) :
  arr[house][0] += min(arr[house-1][1], arr[house-1][2]) # 현재에서 R이 선택될
  arr[house][1] += min(arr[house-1][0], arr[house-1][2]) # 현재에서 G가 선택될
  arr[house][2] += min(arr[house-1][0], arr[house-1][1])

print(min(arr[N-1]))

# -- 그냥 접근 부터 틀린 실패한 풀이 -- #
# dp = [(float('inf'),-1)] * (N+1)
# dp[0] = (0,-1)
# for house in range(1,N) :
#   # 현재단계를 확정짓기 위해서는 그 뒤에를 봐야한다.
#
#   selected = (float('inf'),-1,-1)
#   for cur_color in range(3) :
#     for next_color in range(3) :
#       if cur_color == next_color :
#         continue # 같은색은 고려하지 않는다.
#       next = (arr[house][cur_color] + arr[house+1][next_color], arr[house][cur_color],cur_color)
#       if next[0] < selected[0] :
#         selected = next
#   dp[house] = (dp[house-1][0] + selected[1], selected[2])
#
# result = float('inf')
# print(arr)
# for color in range(3) :
#   if dp[N-1][1] == color :
#     continue
#   result = min(result, dp[N-1][0] + arr[N][color])
# dp[N] = (result,-1)
# print(dp)
