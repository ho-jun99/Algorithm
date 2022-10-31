import sys

BACKE_SPACE = "-"
LEFT = "<"
RIGHT = ">"

# 시간초과 남
def un_solve(n):
  result = []
  for _ in range(n):
    str = ""
    cursor = 0
    logs = sys.stdin.readline().strip()
    q = [logs[i] for i in range(len(logs))]
    for log in q:
      if log == BACKE_SPACE:
        # 커서가 맨 앞일때
        if cursor == 0 :
          continue
        # 커서가 맨 끝일때
        elif cursor == len(str):
          str = str[:cursor-1]
          cursor -=1
        # 커서가 중간일때
        else :
          str = str[:cursor-1] + str[cursor:]
          cursor -=1

      elif log == LEFT:
        if cursor > 0:
          cursor -=1

      elif log == RIGHT:
        if cursor < len(str):
          cursor +=1
      else: # 글을 입력받을때
        # 커서가 맨앞일때
        if cursor == 0:
          str = log + str
        # 커서가 맨뒤일때
        elif cursor == len(str):
          str = str + log
        # 커서가 중간일때
        else:
          str = str[:cursor] + log + str[cursor:]
        cursor+=1
    result.append(str)
  return result

def solve(n):
  result = []
  for _ in range(n):
    logs = sys.stdin.readline().strip()
    q = [logs[i] for i in range(len(logs))]
    left_stack = []
    right_stack = []
    for log in q:
      if log == BACKE_SPACE:
        if len(left_stack) != 0:
          left_stack.pop()

      elif log == RIGHT:
        if len(right_stack) !=0:
          left_stack.append(right_stack.pop())

      elif log == LEFT:
        if len(left_stack) !=0:
          right_stack.append(left_stack.pop())
      else:
        left_stack.append(log)
    str = ""
    for i in left_stack:
      str += i
    for i in reversed(right_stack):
      str +=i
    result.append(str)
  return result

if __name__ == '__main__':
  n = int(input())
  a = solve(n)
  for i in a:
    print(i)
