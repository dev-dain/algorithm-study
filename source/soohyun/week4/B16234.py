# 백준 16234 인구 이동
# https://www.acmicpc.net/problem/16234

from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0] # 동서남북
answer = 0 # 인구 이동 횟수

def bfs(i, j):
    queue = deque([[i, j]])
    move = deque() # 연합한 나라
    visited[i][j] = 1
    cnt, people = 0, 0 # 연합한 나라수, 인구수

    while queue:
        x, y = queue.popleft()
        move.append([x, y])
        cnt += 1
        people += graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]: # 범위 내에 있으며 아직 방문하지 않은 경우
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R: # 인구수 차이가 L이상 R이하라면 연합에 추가
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
    
    # 인구이동이 불가능한 경우
    if cnt == 1:
        return False

    # 인구이동이 가능한 경우
    new = people // cnt
    while move:
        x, y = move.popleft()
        graph[x][y] = new
    return True


while True:
    visited = [[0] * N for _ in range(N)]
    stop = True # 인구이동을 멈출지 여부

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j): # 인구이동이 가능하다면 멈추지 않는다
                    stop = False

    if stop:
        break
    else:
        answer += 1

print(answer)