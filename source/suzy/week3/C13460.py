from collections import deque
import sys
input = sys.stdin.readline
# 세로 N 가로 M
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        # 빨간 구슬 위치
        if graph[i][j] == 'R':
            rx, ry = i, j
        # 파란 구슬 위치
        if graph[i][j] == 'B':
            bx, by = i, j

# 방향 벡터
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx,ry,bx,by))
    # 방문 여부 판단 리스트
    visited = []
    visited.append((rx,ry,bx,by))
    cnt = 0
    while q:
        for i in range(len(q)):
            rx, ry, bx, by = q.popleft()
            # 이동횟수 10회를 넘을 경우 : 실패
            if cnt >10:
                print(-1)
                return
            # 현 위치가 빨강 구슬인데 탈출 구멍일 경우 !
            if graph[rx][ry] == 'O':
                print(cnt)
                return
            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] == '#': # '#' 일 때 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] == 'O':# 구멍일 때
                        break
                
                 # 현 위치가 파란구슬 !
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == 'O':
                        break
                
                # 만약 파란 구슬이 들어가는 경우 무시
                if graph[nbx][nby] == 'O':
                    continue
                
                # 두 구슬의 위치가 같은 경우
                if nrx == nbx and nry == nby:
                    # 더 늦게 이동한 구슬을 제자리로 이동
                    if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx) + abs(nby-by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                
                # 방문 안했다면 큐에 추가
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt += 1
        
    print(-1) # 10회를 초과하지 않아도 성공할 수 없는 경우
bfs(rx, ry, bx, by)