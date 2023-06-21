import sys

arrs = list(map(int,sys.stdin.readline().split()))

result = 0

for arr in arrs :
  result += pow(arr,2)

result %= 10
print(result)