def solution(sequence, k):
    answer = list()
    N = len(sequence)
    left = 0
    right = 0
    sum = sequence[0]
    
    while True : 
        if sum > k :
            sum -= sequence[left]
            left+=1
            if left == N :
                break
        elif sum < k :
            right += 1
            if right == N :
                break
            sum += sequence[right]
        else : # k == sum
            answer.append((right-left,left,[left,right]))
            sum -= sequence[left]
            left+=1
            if left == N :
                break
    
    answer.sort(key= lambda x : (x[0],x[1]))
    a = answer[0][2]
    return a