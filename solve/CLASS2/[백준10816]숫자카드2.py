# n^2 탐색으로 시간초과 남
# 이분탐색을 이용해서 찾아도 시간초과 남
# 애초에 입력받을때 map을 이용
# defaultdic을 사용해서 초기값을 주거나, key in dict.keys()를 사용해서 초기값 설정을 해주면 됨
# 후자는 계속 탐색하기 때문에 느릴수도..?

import sys
from collections import defaultdict

n = int(input())
d = defaultdict(int)
pivot = list(map(int,sys.stdin.readline().split()))
for key in pivot :
    d[key] += 1

m = int(input())
target = list(map(int,sys.stdin.readline().split()))

for i in target:
    print(d[i],end=" ")


