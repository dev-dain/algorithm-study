# 백준 14503 로봇 청소기
# https://www.acmicpc.net/problem/14503

N, M = map(int, input().split())
r, c, d= map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
cnt = 0 # 청소한 칸의 개수

def clean(x, y, d):
    global cnt
    
    # 현재 위치를 청소한다
    if graph[x][y] == 0:
        cnt += 1
        graph[x][y] = 2

    # 네 방향을 확인
    for i in range(4):
        nd = (d + 3) % 4 # 왼쪽 방향
        # 전진할 위치
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0: # 청소 범위이며 아직 청소하지 않았다면 전진
            clean(nx, ny, nd)
            return
        d = nd # 방향 변경

    # 네 방향 모두 이동할 수 없다면
    nd = (d + 2) % 4
    # 후진할 위치
    nx = x + dx[nd]
    ny = y + dy[nd]
    if graph[nx][ny] == 1: # 후진할 수 없는 경우 작동을 멈춘다
        return
    clean(nx, ny, d) # 후진할 수 있다면 방향은 유지한 채 후진

clean(r, c, d)
print(cnt)