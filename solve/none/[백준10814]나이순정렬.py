import sys


# key값으로 정렬을 하는데, 그 외 순서에대해서는 stable속성이 적용된다.
# 즉 원래 순서를 유지하면서 정렬된다.
def solve():
  N = int(input())
  list = []
  for _ in range(N):
    year,name = sys.stdin.readline().strip().split()
    data = (int(year),name)
    list.append(data)
  list.sort(key=lambda x:x[0])
  for age,name in list:
    print(age, name)

if __name__ == '__main__':
    solve()