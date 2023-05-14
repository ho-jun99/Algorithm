'''
  - 문제에서는 Pn이 몇개가 존재하는지 찾아야함
  - Pn의 정의 -> N+1개의 I와 N개의 0
  - KMP 알고리즘을 통해서 찾아보자 ( 문자열 검색을 위한 알고리즘 )
    - Brute Force로 찾으면 O(MN)의 시간복잡도를 가진다.
    - KMP의 접두부, 접미부, 경계부에 대한 이해가 필요함
    - 매칭에 실패했을때 얼마큼 점프해야하는지 알려준다.
  - KMP의 작동방식
    - O(n) 의 시간복잡도를 가진다.

'''


import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

pattern = ""
for i in range((2*n)+1) :
  if i % 2 == 0 : # 짝수 인덱스일때 I 추가
    pattern += "I"
  else :
    pattern += "O"
# print(pattern)

# KMP를 위한 table 만들기
pattern_table = [0] * (len(pattern))
j = 0
for i in range(1,len(pattern_table)) :
  while j > 0 and pattern[i] != pattern[j] :
    j = pattern_table[j-1]
  if pattern[i] == pattern[j] :
    j +=1
    pattern_table[i] = j

# KMP를 통해서 탐색하기
cnt = 0
j = 0
for i in range(len(s)) :
  while j > 0 and s[i] != pattern[j] :
    j = pattern_table[j-1]
  if s[i] == pattern[j] :
    if j == len(pattern)-1 : # 모든 문자열이 일치했다면,
      cnt +=1
      j = pattern_table[j]
    else :
      j+=1

print(cnt)

# # --- 정답 풀이 --- ###
#
# # P_n이 주어진다
# # P_n의 갯수를 찾으면 된다
# # 파이썬 문자열의 find를 활용한다면?
#
# cursor = 0
# cnt = 0
# result = 0
# while cursor < m-2 :
#   if s[cursor:cursor+3] == "IOI" :
#     cursor +=2
#     cnt +=1
#     if cnt == n :
#       result +=1
#       cnt -=1
#   else :
#     cursor += 1
#     cnt = 0
#
# print(result)
#
