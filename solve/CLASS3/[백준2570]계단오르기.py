import sys


# def downstair(num,one_cnt,stair) :
#   if one_cnt<=1 and num == 0 :
#     return 0
#   elif one_cnt>=2 and num == 0 :
#     return -float('inf')
#
#   if one_cnt<=1 and num == 1  :
#     return stair[1]
#   elif one_cnt>=2 and num == 1:
#     return -float('inf')
#
#   if one_cnt >= 2 :
#     return stair[num] + downstair(num-2,0,stair)
#   else :
#     return stair[num] + max(downstair(num-1,one_cnt+1,stair),downstair(num-2,0,stair))
#
#
#
# # change memo
# def up(cur,end,one_cnt,stair) :
#   if cur == end and one_cnt <=2:
#     return stair[cur]
#   elif cur >= end :
#     return -float('inf')
#
#   if one_cnt >= 2 :
#     return stair[cur] + up(cur+2,end,1,stair)
#   else:
#     return stair[cur] + max(up(cur+1,end,one_cnt+1,stair),up(cur+2,end,1,stair))



t = int(sys.stdin.readline())
dp = [0] * (t+1)
stair = list()
stair.append(0)

for _ in range(t):
  stair.append(int(sys.stdin.readline()))

dp[1] = stair[1]
if t == 1 :
  print(dp[1])
  exit()
dp[2] = stair[1] + stair[2]

for i in range(3,t+1) :
  dp[i] = stair[i] + max(dp[i-2], (stair[i-1] + dp[i-3]))

print(dp[t])


