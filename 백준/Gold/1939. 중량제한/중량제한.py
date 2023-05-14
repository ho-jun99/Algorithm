import sys
from collections import deque

def bfs(c):
    q = deque()
    q.append(start)
    check = [False] * (N + 1)
    check[start] = True

    while q:
        x = q.popleft()
        for y, w in adj_list[x]:
            # y섬을 아직 방문하지 않았고, 현재 무게(c)로 갈 수 있으면
            if not check[y] and w >= c:
                check[y] = True
                q.append(y)
    # end 섬에 도달할 경우 True, 아니면 False
    return True if check[end] else False

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        adj_list[a].append((b, c))
        adj_list[b].append((a, c))
    start, end = map(int, sys.stdin.readline().split())
    mx, mn = 1000000000, 1
    ans = 0
    while mn <= mx:
        mid = (mn + mx) // 2
        # mid 무게로 start 섬에서 end 섬으로 갈 수 있을 경우
        # ans 갱신, 최대값을 구하기 위해 mn 증가
        if bfs(mid):
            ans = mid
            mn = mid + 1
        # 못 갈 경우 mx를 줄이면서 갈 수 있는 무게 구하기
        else:
            mx = mid - 1
    print(ans)