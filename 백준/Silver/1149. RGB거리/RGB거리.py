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