def answer(n) :
  if( n<= 3) :
    print(1)
    return
  list = [0 for i in range(n+1)]
  list[1] = 1
  list[2] = 1
  for i in range(3,n+1):
    list[i] = list[i-2] + list[i-3]
  print(list[n])



if __name__ == '__main__':
    times = int(input())
    for i in range(times):
      n = int(input())
      answer(n)
