# 백준 21610 마법사 상어와 비바라기
# https://www.acmicpc.net/problem/21610

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]
# 서, 서북, 북, 동북, 동, 동남, 남, 서남
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud, new_cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]], [] # 현재 구름 위치, 다음 구름 위치

for d, s in move:
    d -= 1
    visited = [[0] * n for _ in range(n)] # 각 위치의 구름 방문 확인 리스트
    loc = [] # 이동한 구름 위치

    # 구름이 이동한 위치의 물의 양이 1 증가
    for x, y in cloud:
        nx = (x + s * dx[d]) % n
        ny = (y + s * dy[d]) % n
        board[nx][ny] += 1
        visited[nx][ny] = 1
        loc.append([nx, ny])
    
    # 물복사 버그 마법으로 해당 위치의 물의 양이 증가
    for x, y in loc:
        for i in [1, 3, 5, 7]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                board[x][y] += 1

    # 다음 구름 위치 구하기
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and visited[i][j] == 0:
                new_cloud.append([i, j])
                board[i][j] -= 2

    cloud, new_cloud = new_cloud, []

print(sum([sum(b) for b in board])) # 물의 양의 합 