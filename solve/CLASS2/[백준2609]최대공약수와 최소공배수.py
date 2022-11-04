import sys

def gcd(a,b):
  if a%b == 0 :
    return b
  return gcd(b,a%b)

arr = list(map(int,sys.stdin.readline().strip().split()))
arr = sorted(arr)
a = arr[1]
b = arr[0]
print(gcd(a,b))
print(a*b // gcd(a,b))




def solve1(a,b) :
  # 최대공약수 구하기
  result = 1
  while True :
    isEnd = False
    for i in range(2,min(a,b)) :
      if( a % i ==0 and b % i == 0) :
        a = a//i
        b = b//i
        result *= i
        break
      if( i == min(a,b)-1) :
        isEnd = True
    if isEnd : break
  print(result)

  # 최소공배수 구하기
  result = 1
  a = copy_a
  b = copy_b
  while True :
    isEnd = False
    for i in range(2,min(a,b)) :
      if( a % i ==0 and b % i == 0) :
        a = a//i
        b = b//i
        result *= i
        break
      if( i == min(a,b)-1) :
        isEnd = True
    if isEnd : break
  print(result*a*b)