import random


def seq_search(list,target):
  for i in range(len(list)) :
    if list[i] == target :
      return True
  return False


if __name__ == '__main__':
    list = random.sample(range(30),10)
    target = 10
    print(f"{list} target {target}")
    answer = seq_search(list,target)
    print(answer)
