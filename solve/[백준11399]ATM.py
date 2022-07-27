import sys

def answer(n,p_list) :
  p_list.sort()
  sum = 0
  for i in range(n) :
    if i == 0 :
      sum += p_list[i]
      continue
    p_list[i] = p_list[i] + p_list[i-1]
    sum += p_list[i]
  return sum

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    p_list = list(map(int,sys.stdin.readline().strip().split()))
    result = answer(n,p_list)
    print(result)