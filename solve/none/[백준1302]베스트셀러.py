import sys

# sorted를 사용해서 key를 사전순으로 정렬 후
# 다시 dict로 타입변경 후 max를 수행

def solve():
  N = int(sys.stdin.readline().strip())
  dic = dict()
  for _ in range(N):
    book = sys.stdin.readline().strip()
    if book not in dic:
      dic[book] = 1
    else :
      dic[book] +=1

  temp = sorted(dic.items())
  temp = dict(temp)
  print(max(temp,key=lambda x: dic[x]))

if __name__ == '__main__':
    solve()