def solve():
  n = int(input())
  fly = 1
  time = 0
  while n > 0:
    if n >= fly :
      n = n - fly
      fly +=1
      time += 1
      # print(f"n {n} fly{fly}")
    else :
      fly = 1
      # print(f"n {n} fly{fly}")

  print(time)

if __name__ == '__main__':
  solve()
