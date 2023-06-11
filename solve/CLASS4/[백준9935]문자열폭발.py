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



# # 시간초과 풀이 ( 리스트 슬라이싱 사용 때문에 ) # #
# s = sys.stdin.readline().strip()
# bomb = sys.stdin.readline().strip()
# bomb_size = len(bomb)
# stk = list()
#
# while len(s) >= bomb_size :
#   # print(s, stk)
#   if s[-bomb_size:] == bomb :
#     s = s[:-bomb_size] # 걷어내고
#
#     # 스택을 확인한다.
#     stkcnt = 0
#     while len(stk) != 0 :
#       s += stk.pop()
#       stkcnt +=1
#       if stkcnt == bomb_size :
#         break
#   else :
#     stk.append(s[-1])
#     s = s[:-1]
#
#
# # print("result")
# # print(s,stk)
#
# for ch in s :
#   stk.append(ch)
#
# if len(stk) == 0 :
#   print("FRULA")
# else :
#   for c in reversed(stk) :
#     print(c,end="")
