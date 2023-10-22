from heapq import *

def converter(time) :
    t = time.split(':')
    return int(t[0]) * 60 + int(t[1])


def solution(book_time):
    heap = list()
    lastEnd = [-10]
    answer = 0
    for item in book_time :
        start = converter(item[0])
        end = converter(item[1])
        heappush(heap,(start,end))
        
        
    while heap :
        nowStart, nowEnd = heappop(heap)
        if nowStart >= lastEnd[0] + 10 :
            heappop(lastEnd)
            heappush(lastEnd, nowEnd)
        else :
            heappush(lastEnd, nowEnd)
            
    return len(lastEnd)