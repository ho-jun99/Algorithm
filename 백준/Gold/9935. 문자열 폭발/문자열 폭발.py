import sys

s = list(sys.stdin.readline().strip())
bomb = list(sys.stdin.readline().strip())
bomb_size = len(bomb)
stk = list()

clear_cnt = 0
bomb_idx = bomb_size-1
temp = 0
while len(s) != 0:
  temp +=1
  s_poped = s.pop()
  stk.append(s_poped)

  # print(s, stk)

  if len(stk) >= bomb_size :
    if stk[-bomb_size:] == bomb[::-1] :
      for _ in range(bomb_size) :
        stk.pop()

      stk_cnt = 0
      while len(stk) != 0 :
        s.append(stk.pop())
        stk_cnt+=1
        if stk_cnt == bomb_size :
          break

# print("Result")
# print(s, stk)
for ch in reversed(s) :
  stk.append(ch)


if len(stk) == 0 :
  print("FRULA")
else :
  for i in reversed(stk) :
    print(i,end="")
