'''
  - 수열의 크기 N이 최대 1,000이기 때문에 O(N^2)을 이용한 완전탐색을 하더라도
    1,000,000 ( 약 백만 ) 안에 구할 수 있기 때문에 1초안에 구할 수 있을 것으로 보인다.
'''
import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))

dp = [1] * (N+1)
for pivot in range(N) :
  for j in range(pivot) :
    if arr[j] < arr[pivot] :
      dp[pivot] = max(dp[pivot], dp[j]+1)

print(max(dp))