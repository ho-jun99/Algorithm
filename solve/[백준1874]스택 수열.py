"""
  해당 수가 나올 때까지 push하기
"""
import sys

PLUS = "+"
MINUS = "-"

# 실패 코드
def get_top(stack):
  stack_len = len(stack)
  if stack_len == 0:
    return 0
  return stack[stack_len-1]

def get_start(stack):
  if len(stack) == 0 :
    return 0
  return stack[0]

def not_solve(n,seq):
  default = [i for i in range(1,n+1)]
  stack = []
  result = []

  for seq_num in seq:
    print(result)
    if get_start(default) < seq_num:
      while True:
        if len(default) == 0 :
          continue
        pop = default.pop(0)
        stack.append(pop)
        result.append(PLUS)
        if pop == seq_num:
          stack.pop()
          result.append(MINUS)
          break

    elif get_start(default) > seq_num:
      if get_top(stack) == seq_num:
        stack.pop()
        result.append(MINUS)
      else:
        return "NO"
    elif len(default) == 0:
      if seq_num == get_top(stack):
        stack.pop()
        result.append(MINUS)
      else:
        return "NO"
  return result


# 정답 코드
def solve(n,seq):
  count = 1
  stack = []
  result = []
  for i in range(n):
    data = seq.pop(0)
    while count <= data:
      stack.append(count)
      result.append(PLUS)
      count+=1
    if stack[-1] == data:
      stack.pop()
      result.append(MINUS)
    else:
      return "NO"
  return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    seq = []
    for i in range(n):
      seq.append(int(sys.stdin.readline().strip()))

    a = solve(n,seq)
    if a == "NO":
      print(a)
    else:
      for i in a:
        print(i)
