import sys


def solve():
  N = int(sys.stdin.readline().strip())
  arr = []
  for _ in range(N):
    tropi = int(sys.stdin.readline().strip())
    arr.append(tropi)

  max = 0
  cnt = 0
  # 순회하면서 max값이 갱신되면 보이는 거임
  # LEFT
  for item in arr:
    if item > max :
      cnt +=1
      max = item
  print(cnt)

  # RIGHT
  max = 0
  cnt = 0

  for item in reversed(arr):
    if item > max :
      cnt +=1
      max = item

  print(cnt)


if __name__ == '__main__':
  solve()
