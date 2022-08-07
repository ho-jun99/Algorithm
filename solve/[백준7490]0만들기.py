def zero2(start,n,result,end):
  if start == n:
    if result == 0:
      return print(end)
    return
  next = start+1

  str_plus = end + "+" + str(next)
  zero(next,n,result+next,str_plus)

  str_minus = end + "-" + str(next)
  zero(next,n,result-next,str_minus)

여기서 틀려져버림ㅠㅠ
  str_empty = end + " " + str(next)
  zero(next,n,start*10+next,str_empty)

result = []

def zero(target,n,text):
  if target == n :
    if eval(text.replace(" ","")) == 0 :
      return print(text)
    return

  next = target+1
  # empty
  str_empty = text + " " + str(next)
  zero(target+1,n,str_empty)

  # plus
  str_plus = text + "+" + str(next)
  zero(target+1,n,str_plus)

  # minus
  str_minus = text + "-" + str(next)
  zero(target+1,n,str_minus)

def solve():
  case = int(input())
  for _ in range(case):
    N = int(input())
    zero(1,N,"1")
    print()


if __name__ == '__main__':
    solve()