import sys

def solve():
  N, K = map(int, sys.stdin.readline().strip().split())
  arr = list(map(int, sys.stdin.readline().strip().split()))
  print(sorted(arr)[K-1])

if __name__ == '__main__':
  solve()
