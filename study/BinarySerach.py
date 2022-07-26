# 이진탐색은 데이터셋이 정렬되어 있어야함.
import random

def binary_serach(list,target):
  print(f"{list}, target : {target}",end="")
  # 찾는 조건
  if len(list) == 1 :
    if list[0] == target :
      return True
    else :
      return False
  elif len(list) == 0 :
    # binary_serach함수를 호출할때 list[mid+1:]로 슬라이싱 하기 때문에
    # len이 0이 되는 경우가 존재
    return False

  # 탐색 조건
  mid = len(list) // 2
  print(f", mid {list[mid]}")
  if target == list[mid] :
    return True
  elif target < list[mid] :
    return binary_serach(list[:mid],target)
  elif target > list[mid] :
    return binary_serach(list[mid+1:],target)



if __name__ == '__main__':
  list = random.sample(range(20), 10)
  list.sort()
  answer = binary_serach(list, 10)
  print(answer)