
# 재귀 이용했더니 시간초과 뜸
def fibo(n):
  if n <= 1:
    return n
  return fibo(n-1) + fibo(n-2)

def solve():
  n = int(input())
  print(fibo(n))


def solve2():
  n = int(input())
  memo = [0,1]
  for index in range(2,n+1):
    memo.append(memo[index-1] + memo[index-2])
  print(memo[n])

if __name__ == '__main__':
    solve2()
