from collections import defaultdict

def solution(s):
    answer = []
    dic = {}
    
    for index,item in enumerate(s):
        if item not in dic :
            answer.append(-1)
        else :
            distance = index - dic[item]
            answer.append(distance)
        dic[item] = index
        
    return answer