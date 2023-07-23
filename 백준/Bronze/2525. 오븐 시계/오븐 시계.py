import sys
hour,minute = map(int,sys.stdin.readline().split()) # 0 ~ 23
time = int(sys.stdin.readline())

t_h = time // 60
t_m = time % 60

hour += t_h
minute += t_m

if minute >= 60 :
  hour += 1
  minute = minute % 60

if hour >= 24 :
  hour = hour % 24

print(hour, minute)