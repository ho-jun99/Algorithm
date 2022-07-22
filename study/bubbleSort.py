import random

def swap(data,index):
  temp = data[index + 1]
  data[index + 1] = data[index]
  data[index] = temp
  print(data, index)

def bubble_sort(input):
  size = len(input)
  data = input
  print(f"size {size}")
  for turn in reversed(range(size)):
    print(f"######### {turn}")
    for index in range(turn):
      if (input[index] > input[index + 1]):
        swap(data,index)
  print(f" sorted {data}")

if __name__ == '__main__':
  input = random.sample(range(100), 10)
  print(f"sample data : {input}")
  bubble_sort(input)