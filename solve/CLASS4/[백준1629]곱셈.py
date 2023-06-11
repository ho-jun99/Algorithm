import sys

A,B,C = map(int,sys.stdin.readline().split())

# A를 B번곱한수를 C로 나눈값
# O(logN)을 가지는 곱셈법을 사용해서 구해야 한다.

def power(a,b) :
  if b == 0 :
    return 1
  if b % 2 == 0 : # 짝수일때
    temp = b//2
    result = power(a,temp) % C
    return result*result
  else : # 홀수 일때
    temp = b//2
    result = power(a,temp) % C
    return result*result*a

print(power(A,B) % C)

