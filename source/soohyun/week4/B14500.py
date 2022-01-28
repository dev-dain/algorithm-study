# 백준 14500 테트로미노
# https://www.acmicpc.net/problem/14500

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
visited = [[0] * M for _ in range(N)]
ans = 0 # 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값
max_value = max(map(max, graph)) # 종이에 있는 수의 최대값

def dfs(x, y, n, total):
    global ans

    # 현재 합의 최대값을 갱신할 수 없는 경우 탐색을 그만둔다
    if ans >= total + max_value * (3 - n):
        return

    # 테트로미노가 완성되면 합의 최대값을 갱신한다
    if n == 3:
        ans = max(ans, total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어나지 않으며 아직 방문하지 않는 경우 정사각형을 놓는다
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            if n == 1: # ㅗ 모양인 경우
                dfs(x, y, n+1, total + graph[nx][ny])
            dfs(nx, ny, n+1, total + graph[nx][ny])
            visited[nx][ny] = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j, 0, graph[i][j])
            visited[i][j] = 0
print(ans)