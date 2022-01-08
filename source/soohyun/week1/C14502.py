# 백준 14502 연구소
# https://www.acmicpc.net/problem/14502

from collections import deque
import copy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
answer = 0 # 안전영역 크기의 최대값

# 벽 세우기
def wall(w):
    if w == 3: # 벽이 3개 세워지면 바이러스를 퍼지게 한다
        bfs()
        return

    # 벽이 3개 미만이라면 벽을 세운다
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(w+1)
                graph[i][j] = 0 # 초기화

# 바이러스 퍼지게 한 후 안전영역 크기 구하기
def bfs():
    global answer
    g = copy.deepcopy(graph)
    queue = deque()
    
    # 바이러스 위치를 큐에 삽입
    for i in range(N):
        for j in range(M):
            if g[i][j] == 2:
                queue.append([i, j])

    # 바이러스를 퍼지게한다
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if g[nx][ny] == 0:
                    queue.append([nx, ny])
                    g[nx][ny] = 2

    # 안전영역 크기의 최대값을 구한다
    count = 0
    for x in g:
        count += x.count(0)
    answer = max(answer, count)

wall(0) # 벽을 세운 후 바이러스를 퍼지게 하여 안전 영역의 최대값을 구한다
print(answer)