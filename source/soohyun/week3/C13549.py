# 백준 13549 숨바꼭질 3
# https://www.acmicpc.net/problem/13549

from collections import deque

N, K = map(int, input().split())

def bfs(start):
    queue = deque([[start, 0]])
    visited = [0] * 100001
    visited[start] = 1

    while queue:
        loc, time = queue.popleft()
        if loc == K: # 동생을 찾으면 리턴
            return time
        
        # 순간 이동 - 우선순위 0
        if loc < 50001 and visited[loc*2] == 0:
            queue.appendleft([loc*2, time])
            visited[loc*2] = 1
        # x-1 이동 - 우선순위 1
        if loc > 0 and visited[loc-1] == 0:
            queue.append([loc-1, time+1])
            visited[loc-1] = 1
        # x+1 이동 - 우선순위 2
        if loc < 100000 and visited[loc+1] == 0:
            queue.append([loc+1, time+1])
            visited[loc+1] = 1

print(bfs(N))