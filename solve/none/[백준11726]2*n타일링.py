def answer(n):
  if (n <= 1) :
    return 1
  list = [0 for i in range(n + 1)]
  list[1] = 1
  list[2] = 2
  for i in range(3, n + 1):
    list[i] = list[i - 1] + list[i - 2]
  return list[n] % 10_007


if __name__ == '__main__':
  solve = answer(int(input()))
  print(solve)
