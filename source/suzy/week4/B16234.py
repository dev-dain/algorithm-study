from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())

ingu = [ list(map(int, input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i, j):    
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    
    # 연합 국가와 연합국가 총 인원
    move = [(i,j)]
    people = ingu[i][j]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny <0 or nx>=N or ny>= N:
                continue
            if visited[nx][ny]:
                continue
            # L 이상 R 이하일 경우 연합 국가
            if L <= abs(ingu[nx][ny]-ingu[x][y]) <= R:
                q.append((nx,ny))
                visited[nx][ny] = True
                move.append((nx,ny))
                people += ingu[nx][ny]
    # 연합 인구 : 이동인구 총 합 // 이동 국가 수               
    for x, y in move:
        ingu[x][y] = people // len(move)
    
    return len(move)

# 인구 이동 일수
cnt = 0
# 인구 이동이 없을때까지 반복
while True:
    visited = [[False]*N for _ in range(N)]
    # 이동 존재 유무
    flag = False
    # bfs 모든 국가 확인
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i,j) > 1:
                    flag = True
    
    # 인구이동이 없다면
    if not flag:
        break
    cnt += 1
print(cnt)
    