def solve():
  N = input()
  list = []
  for i in range(len(N)):
    list.append(N[i])
  list.sort(reverse=True)

  for i in list:
    print(i,end="")

# 큰수부터 출력해야함으로, 9~0까지 target을 정하고
# 해당 target에 대해서 입력값에 대해서 순회를 진행함
# target이라면 출력함
def solve2():
  N = input()
  for i in range(9,-1,-1):
    for j in N:
      if i == int(j):
        print(i,end="")

if __name__ == '__main__':
    solve2()