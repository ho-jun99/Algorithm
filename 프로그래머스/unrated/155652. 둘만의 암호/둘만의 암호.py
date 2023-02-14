def solution(s, skip, index):
    answer = ''
    baseStart = ord('a')
    baseEnd = ord('z')
    
    for i in range(len(s)) :
        target = s[i]
        cur = ord(target)
        
        for j in range(index):
            cur = cur + 1
            if cur > baseEnd :
                cur = baseStart
                
            while True :
                if chr(cur) in skip :
                    cur = cur +1
                    if cur > baseEnd :
                        cur = baseStart
                else :
                    break
                    
        answer += chr(cur)
                
    
    return answer