def solve():
  n = int(input())
  list = []
  for _ in range(n):
    N = int(input())
    list.append(N)

  for i in sorted(list):
    print(i)

if __name__ == '__main__':
  solve()
