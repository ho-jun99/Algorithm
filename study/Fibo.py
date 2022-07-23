def fibo(num):
  if (num == 0 ) :
      return 0
  if (num == 1 ) :
      return 1
  return fibo(num-1) + fibo(num-2)

# 동적계획법 ( Dynamic Programming)
def dynamic_fibo(num):
    cache = [-1 for i in range(num+1)]
    print(f"cache init {cache}")
    cache[0] = 0
    cache[1] = 1
    for index in range(2,num+1) :
        cache[index] = cache[index-2] + cache[index-1]
        print(cache)
    return cache[num]



if __name__ == '__main__':
    answer = dynamic_fibo(10)
    print(f"answer {answer}")