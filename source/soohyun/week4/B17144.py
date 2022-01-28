# 백준 17144 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

import copy

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
cleaner = [] # 청소기 위치
answer = 0 # 최종 미세먼지 양

# 청소기 위치 구하기
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            cleaner.append([i, j])

# 미세먼지 확산하기
def diff():
    dust = [[0] * C for _ in range(R)] # 확산되는 미세먼지 양

    for x in range(R):
        for y in range(C):
            if graph[x][y] > 0: # 미세먼지인 경우
                d = graph[x][y] // 5 # 확산되는 양
                # 인접한 네방향 확인
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 범위를 벗어나지 않으며 청소기가 아닌 경우 확산될 미세먼지 양을 구한다
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                            dust[nx][ny] += d
                            dust[x][y] -= d

    # 확산되는 미세먼지 양으로 변경시킨다
    for i in range(R):
        for j in range(C):
            graph[i][j] += dust[i][j]

# 미세먼지 이동하기
def move(x, y, dir):
    temp = copy.deepcopy(graph)
    cx, cy = x, y
    temp[x][y] = 0 # 청소기 위치는 0으로

    # 청소기 이동 방향대로 이동시킨다
    for i in range(4):
        while True:
            nx = x + dx[dir[i]]
            ny = y + dy[dir[i]]
            if nx == cx and ny == cy: # 청소기 위치라면 이동을 멈춘다
                return
            if nx < 0 or nx >= R or ny < 0 or ny >= C: # 범위를 벗어나면 다음 방향으로 넘어간다
                break
            graph[nx][ny] = temp[x][y]
            x, y = nx, ny # 다음 칸으로 이동


# T초 동안 확산 -> 이동
for _ in range(T):
    diff()
    move(cleaner[0][0], cleaner[0][1], [1, 0, 3, 2])
    move(cleaner[1][0], cleaner[1][1], [1, 2, 3, 0])

for i in range(R):
    for j in range(C):
        if graph[i][j] != -1:
            answer += graph[i][j]
print(answer)