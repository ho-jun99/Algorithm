import sys

def solve():
  N = int(sys.stdin.readline().strip())
  arr = []
  for _ in range(N):
    arr.append(int(sys.stdin.readline().strip()))

  arr.sort()
  for i in arr:
    print(i)

if __name__ == '__main__':
    solve()
