# 백준 16236 아기 상어
# https://www.acmicpc.net/problem/16236

from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
sx, sy = 0, 0 # 상어의 위치
size, time, eat = 2, 0, 0 # 상어 크기, 최소 이동 시간, 먹은 물고기 수

def bfs():
    global sx, sy, size, time, eat

    while True: # 더 이상 먹을 수 있는 물고기가 없을 때까지
        queue = deque([[sx, sy, 0]])
        visited = [[0] * N for _ in range(N)]
        visited[sx][sy] = 1
        fish = [] # 먹을 수 있는 물고기
        flag = 1e9 # 최소 이동 시간

        while queue:
            x, y, cnt = queue.popleft() # 위치, 이동시간
            if cnt > flag: # 최소 이동 시간보다 오래 걸리는 경우 = 먹을 수 있는 물고기를 찾은 경우
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N: # 이동 범위를 벗어난 경우
                    continue
                if visited[nx][ny] or graph[nx][ny] > size: # 방문 했거나 상어 크기보다 큰 경우
                    continue
                if graph[nx][ny] != 0 and graph[nx][ny] < size: # 물고기가 있는 위치이며 물고기 크기가 상어 크기보다 작은 경우
                    fish.append([nx, ny, cnt+1]) # 먹을 수 있는 물고기에 추가
                    flag = cnt # 최소 이동 시간 초기화
                # 지나갈 수 있는 경우 방문 처리
                queue.append([nx, ny, cnt+1])
                visited[nx][ny] = 1
        
        if fish:
            fish.sort() # 위, 왼쪽 물고기부터 먹어야 하므로 정렬
            x, y, t = fish.pop(0)
            time += t
            eat += 1
            graph[x][y] = 0 # 물고기를 먹은 위치는 빈칸으로 초기화
            # 먹은 물고기 수가 상어 크기와 같다면 크기를 키운다
            if eat == size:
                size += 1
                eat = 0
            sx, sy = x, y # 상어 위치 이동
        else: # 먹을 수 있는 물고기가 없는 경우
            break

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            graph[i][j] = 0
            sx, sy = i, j
            break

bfs()
print(time)