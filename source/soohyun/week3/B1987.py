# 백준 1987 알파벳
# https://www.acmicpc.net/problem/1987

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(i, j):
    queue = set([(i, j, graph[0][0])])
    cnt = 0 # 지나갈 수 있는 최대 칸수

    while queue:
        x, y, visited = queue.pop() # 현재 위치, 방문한 알파벳 리스트
        cnt = max(cnt, len(visited)) # 최대칸수 구하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in visited: # 범위 내에 있으며 아직 방문하지 않은 알파벳이라면 큐에 삽입
                new_visited = visited + graph[nx][ny]
                queue.add((nx, ny, new_visited))
                
    return cnt

answer = bfs(0, 0)
print(answer)