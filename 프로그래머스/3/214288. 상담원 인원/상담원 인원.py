from itertools import permutations
import heapq
import copy

candidates = list()

def dfs(depth, k, n, arrs) :
    if n < sum(arrs) : return
    if depth == k : # 상담 유형만큼만 뽑아야한다.
        if sum(arrs) == n :
            candidates.append(copy.deepcopy(arrs))
            return
    
    for i in range(1,n-k+2) :
        arrs.append(i)
        dfs(depth+1, k, n, arrs)
        arrs.pop()

def solution(k, n, reqs):
    global candidates
    answer = 0
    # k : 상담 유형, n : 멘토 명수, reqs : 상담요청
    # 순열로 k(상담유형)을 뽑고, 완탐을 돌려서 최소 시간을 구한다.
    dfs(0, k, n, [])
    
    # 유형별 멘토인원 배열이 candidates에 할당됐다.
    result = float('inf')
    for case in candidates : 
        queues = [ [] for i in range(k)]
        casePerWatingTime = 0
        for req in reqs : 
            start, duration, queueType = req
            queueType -=1 # 값 보정
            if case[queueType] > 0 :
                # heap에다가 삽입한다.
                case[queueType] -=1
                heapq.heappush(queues[queueType],(start+duration, start, duration, queueType))
            else : 
                # 공간이 없을 경우 빼야한다.
                popedEndTime, popedStart, popedDuration, popedQueueType = heapq.heappop(queues[queueType])
                
                # 끝낸 회의의 EndTime과, 지금 시작하는 회의 시작 시간을 확인한다.
                if popedEndTime <= start : # 따로 기다린 것이 아니다.
                    heapq.heappush(queues[queueType], (start + duration, start, duration, queueType))
                else : # 기다린거라면, 기다린 시간을 구한다.
                    casePerWatingTime += popedEndTime - start # 기다린 시간
                    heapq.heappush(queues[queueType], (popedEndTime + duration, popedEndTime, duration, queueType))
                
                
        result = min(result,casePerWatingTime)

    answer = result
    return answer