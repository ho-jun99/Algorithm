import random

def selection_sort(data):
  size = len(data)
  for target in range(size):
    min_index = target
    for index in range(target + 1, size):
      if (data[min_index] > data[index]):
        min_index = index
    #swap
    temp = data[min_index]
    data[min_index] = data[target]
    data[target] = temp


if __name__ == '__main__':
  input = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  sample_list = random.sample(range(10),10)

  # test
  print(f"before {sample_list}")
  selection_sort(sample_list)
  print(f"sorted {sample_list}")
