import random


def insertion_sort(input):
  data = input
  size = len(data)
  for target in range(1, size):
    copy_target = data[target]
    for index in range(target-1, -1, -1):
      if (copy_target < data[index]):
        data[index+1] = data[index]
        data[index] = copy_target
      else:
        break


if __name__ == '__main__':
  input = [10,9,8,7,6,5,4,3,2,1,0]
  insertion_sort(input)
  print(input)

