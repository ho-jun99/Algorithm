import sys

inorders = list((sys.stdin.readline().strip()))
# print(inorders)

# 생각해낸 풀이 ( 좋은 방법은 아니다. inorder를 트리 관계로 표현하는거 부터가 너무 힘들다.가능은 할까? )
  # inorder를 트리의 관계로 표현시킨 뒤
  # postorder를 돌리면 될거 같다. 대신 '(' , '(' 괄호를 생략시면 될듯 하다.
# 스택을 이용하면 풀 수 있다고 한다.

operators = ["+", "-", "*", "/"]
stk = list()
result = ""

def compare_operatior(cur,stacktop) :
  if stacktop == "(" or stacktop == ")" :
    return 1 # 우선순위가 무조건 더 크다 근데 이떄는 pop하면 안된다.

  if cur == "*" or cur == "/" :
    if stacktop == "*" or stacktop == "/" :
      return -1 # 우선순위가 똑같다.
    else :
      return 1 # 우선순위가 더 크다.
  else : # cur이 "+"와 "-"인 경우
    if stacktop == "+" or stacktop == "-" :
      return  -1 # 우선순위가 똑같다.
    else:
      return -1 # 우선순위가 작다.

for token in inorders :
  if token in operators : # 연산자일 경우에
    while True :
      if len(stk) == 0 :
        stk.append(token)
        break
      top = stk[len(stk) - 1]  # 최상위 위치를 확인
      if compare_operatior(token,top) == 1 : # 우선순위가 더 크다
        stk.append(token)
        break
      elif compare_operatior(token,top) == -1 : # 우선순위가 작거나 똑같을 경우
        result += stk.pop()


  elif token == "(" :
    stk.append(token)

  elif token == ")" : # 닫는 괄호 일 경우

    while len(stk) != 0 :
      top = stk[len(stk)-1] # 최상위를 확인
      if top == "(" :
        stk.pop()
        break
      else :
        result += stk.pop()

  else : # 피연산자일 경우
    result += token
  # print(f"result : {result}, stk : {stk}")

while len(stk) != 0:
  top = stk[len(stk) - 1]  # 최상위를 확인
  if top == "(":
    stk.pop()
    break
  else:
    result += stk.pop()

# print(f"LAST : result : {result}, stk : {stk}")
print(result)