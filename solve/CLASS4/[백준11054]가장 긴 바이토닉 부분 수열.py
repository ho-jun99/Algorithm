import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))

# print(arr)
# 왼쪽부터 증가하는 수열을 구한다.
dpL = [1] * n
for pivot in range(n) :
  for i in range(pivot) :
    if arr[i] < arr[pivot] :
      dpL[pivot] = max(dpL[pivot], dpL[i] + 1)
# print(dpL)

# 오른쪽부터 증가하는 수열을 구한다.
dpR = [1] * n
for pivot in range(n-1,-1,-1) :
  for i in range(n-1,pivot,-1) :
    if arr[i] < arr[pivot] :
      dpR[pivot] = max(dpR[pivot], dpR[i]+1)
# print(dpR)

# dpL과 dpR의 합을 구한뒤 -1을 하자
 # 1의 값은 중복되기 때문에 빼줘야 한다
for i in range(len(dpL)) :
  dpR[i] = dpL[i] + dpR[i]

print(max(dpR)-1)