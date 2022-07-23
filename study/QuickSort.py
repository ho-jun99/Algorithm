import random

def qsort(list):
  # print("qsort called!")
  if len(list) <= 1 :
    return list
  left,right = [],[]
  pivot = list[0]
  for i in range(1,len(list)):
    if pivot > list[i] :
      left.append(list[i])
    else :
      right.append(list[i])
  return qsort(left) + [pivot] + qsort(right)


if __name__ == '__main__':
  # sample = [4, 3, 7, 2, 6, 8, 9, 0, 1, 5]
  data = random.sample(range(10),10)
  print(data)
  answer = qsort(data)
  print(answer)