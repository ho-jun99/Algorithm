result = float('inf')

def dfs(picks, minerals, depth, cost) :
    global result
    if depth*5 >= len(minerals) :
        result = min(result, cost)
        return 
    
    if picks[0] == 0 and picks[1] == 0 and picks[2] == 0 :
        result = min(result, cost)
        return

    for i in range(3) :
        if picks[i] > 0 :
            scopeCost = 0
            picks[i] -= 1 # 해당 곡갱이를 사용한다.
            # 사용되는 채굴값을 계산한다.
            if i == 0 :
                for mineral in minerals[depth*5 : (depth*5) + 5 ] :
                    if mineral == 'diamond' :
                        scopeCost +=1
                    if mineral == 'iron' :
                        scopeCost +=1
                    if mineral == 'stone' :
                        scopeCost +=1
            if i == 1 :
                for mineral in minerals[depth*5 : (depth*5) + 5 ] :
                    if mineral == 'diamond' :
                        scopeCost += 5
                    if mineral == 'iron' :
                        scopeCost +=1
                    if mineral == 'stone' :
                        scopeCost +=1
            if i == 2 :
                for mineral in minerals[depth*5 : (depth*5) + 5 ] :
                    if mineral == 'diamond' :
                        scopeCost += 25
                    if mineral == 'iron' :
                        scopeCost += 5
                    if mineral == 'stone' :
                        scopeCost +=1
            dfs(picks, minerals, depth +1, cost + scopeCost)
            picks[i] +=1 # 다시 돌려놓는다.
    
def solution(picks, minerals):
    answer = 0
    # 순열을 이용해 diamond를 사용해보자
    dfs(picks, minerals, 0 , 0)
    return result