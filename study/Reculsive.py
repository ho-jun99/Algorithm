import random


def sum_list(data):
  sum = 0
  for i in data:
    sum += i
  return sum


def reculsive_sum(data):
  if len(data) == 1:
    return data[0]
  return data[0] + reculsive_sum(data[1:])


# abcd
# abcde

# 회문 검사
def palindrome(str):
  for index in range( len(str) // 2 ):
    if (str[index] != str[-(index+1)]):
      return False
  return True

# 재귀 회문 검사
def reculsive_palindrome(str):
  if len(str) <= 1:
    return True
  else:
    if(str[0] == str[-1]):
      return reculsive_palindrome(str[1:-1])
    else:
      return False

if __name__ == '__main__':
    str = "level123"
    print(palindrome(str))
    print(reculsive_palindrome(str))

