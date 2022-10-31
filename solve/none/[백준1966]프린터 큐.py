"""
  M을 실시간으로 관리해줘야할 거 같음.
  M이 아닌 다른 문서가 pop이나 재배치가 일어날경우 -1
  M이 맨뒤로 갈경우 + 맨앞에 있는 인덱스 만큼
  즉 M의 인덱스가 0이 되는 경우를 주의깊게 살펴봐야함
"""
import sys

def unsolve(n):
  result = []
  for _ in range(n):
    cnt = 0
    N,M = list(map(int, sys.stdin.readline().strip().split()))
    data = list(map(int, sys.stdin.readline().strip().split()))
    # print(N,M,data,result)
    if N == 1 :
      result.append(1)
      continue

    while M != -1:
      target = data[0]
      if M == 0:
        for i in range(1,len(data)):
          if target < data[i]:
            pop_data = data.pop(0)
            data.append(pop_data)
            M += len(data)-1
            break
          if i == len(data)-1:
            cnt+=1
            result.append(cnt)
            M = -1
      else:
        for i in range(1, len(data)):
          if target < data[i]:
            pop_data = data.pop(0)
            data.append(pop_data)
            M -= 1
            break

          if i == len(data)-1:
            data.pop(0)
            M -=1
            cnt+=1
  return result


# n을 안바꿨네.........
def solve(n):
  result = []
  for _ in range(n):
    cnt = 0
    break_flag = True
    N, M = list(map(int, sys.stdin.readline().strip().split()))
    data = list(map(int, sys.stdin.readline().strip().split()))
    data = [(item,index) for index,item in enumerate(data)]

    while break_flag:
      for i in range(0, len(data)):
        if data[0][0] < data[i][0]:
          # 뒤에 큰게 하나라도 있으면 맨뒤로 보냄
          data.append(data.pop(0))
          break
        if i == len(data)-1:
          #끝까지 탐색했는데도 제일 큰거인 경우
          if data[0][1] == M:
            # 그게 M인경우 M을 출력하고 While문을 멈추게 해야함
            cnt +=1
            result.append(cnt)
            break_flag = False
            break
          else:
            data.pop(0)
            cnt+=1
  return result

if __name__ == '__main__':
  n = int(input())
  a = unsolve(n)
  for i in a:
    print(i)