import math
import sys

a,b,v = map(int,sys.stdin.readline().split())

day = (v-b) / (a-b)
print(math.ceil(day))