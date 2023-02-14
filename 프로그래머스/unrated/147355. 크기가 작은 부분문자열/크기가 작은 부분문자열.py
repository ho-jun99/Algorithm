def solution(t, p):
    answer = 0
    size = len(p)
    for i in range(len(t)-size+1):
        cur = int(t[i:i+size])
        if cur <= int(p) :
            answer +=1
    
    return answer