# 백준 11559 Puyo Puyo
# https://www.acmicpc.net/problem/11559

from collections import deque
import sys

input = sys.stdin.readline
graph = [list(input()) for _ in range(12)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
ans = 0 # 연쇄 횟수

# 뿌요 없애기
def bfs(i, j, state):
    queue = deque([[i, j]])
    puyo = [[i, j]] # 같은 색의 뿌요 리스트
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위에 있고 아직 방문하지 않은 뿌요이며 현재 뿌요와 색깔이 같은 경우
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and graph[nx][ny] == state:
                queue.append([nx, ny])
                puyo.append([nx, ny])
                visited[nx][ny] = 1

    # 같은 색의 뿌요가 4개 이상이면 없앤다
    if len(puyo) >= 4:
        for x, y in puyo:
            graph[x][y] = '.'
    
    return len(puyo)

# 뿌요가 아래로 떨어지기
def down():
    for j in range(6):
        for i in range(10, -1, -1):
            for k in range(11, i, -1):
                if graph[i][j] != '.' and graph[k][j] == '.':
                    graph[k][j] = graph[i][j]
                    graph[i][j] = '.'
                    break

while True:
    visited = [[0] * 6 for _ in range(12)]
    flag = True # 터트릴 뿌요가 없는지 체크

    # 뿌요 없애기
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and graph[i][j] != '.':
                if bfs(i, j, graph[i][j]) >= 4: # 터트릴 뿌요가 있다면 flag = False
                    flag = False

    if flag: break

    ans += 1
    down() # 뿌요 아래로 떨어지기

print(ans)