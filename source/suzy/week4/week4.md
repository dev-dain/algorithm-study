## 4주차
### 1) [백준 14500] (https://www.acmicpc.net/problem/14500)
- 문제 유형:
- 시간 복잡도: O(n*m)  |  공간 복잡도: O(n)
- 접근 방법
    - 인터넷에 여러 풀이를 찾아봤습니다 
    - 직접 모든 경우의 수와 비교하는 방법과 dfs 풀이 두가지가 존재했습니다
<br/><br/>
* 풀이
  * 길이가 4인 경우는 dfs 를 이용하여 구할 수 있습니다
  * 길이가 4이지만 dfs 로 구할 수 없는 경우 (ㅜㅏㅓㅗ) 예외를 따로 구해줍니다
<br/><br/>
- 코드
```python
import sys
input = sys.stdin.readline

# 세로 n 가로 m
n, m  = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]
visited = [[False]*m for _ in range(n)]
answer = 0

# 상우하좌
move = ((-1, 0), (1, 0), (0, -1), (0, 1))

def dfs(x,y,value,length):
    global answer
    
    if length >= 4:
        answer  = max(answer, value)
        return 
    
    for d in move:
        nx = x + d[0]
        ny = y + d[1]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = True
            
            # 다음 지점 호출
            dfs(nx, ny, value + graph[nx][ny], length+1)
            visited[nx][ny] = False

def exception_shape(x, y, value):
    # ㅗㅜㅏㅓ 체크
    global answer
    # ㅗ
    if 0<=x+2<n and 0<= y+1<m:
        value = graph[x][y] + graph[x+1][y] + graph[x+1][y+1] + graph[x+2][y]
        answer = max(answer, value)
    # ㅜ
    if 0<=x-1 and x+1<n and 0<=y+1<m:
        value = graph[x-1][y+1] + graph[x][y+1] + graph[x][y] + graph[x+1][y+1]
        answer = max(answer, value)
    # ㅏ
    if 0<=x+1<n and 0<=y+2<m:
        value = graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y+1]
        answer = max(answer, value)
    # ㅓ
    if 0<=x-1 and x<n and 0<=y+2<m:
        value = graph[x][y] + graph[x-1][y+1] + graph[x][y+1] + graph[x][y+2]
        answer = max(answer, value)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j, graph[i][j], 1)
        visited[i][j] = False
        
        exception_shape(i,j, graph[i][j])
print(answer)
```
---

### 2) [백준 16234] (https://www.acmicpc.net/problem/16234)
- 문제 유형: 구현, 그래프, 시뮬레이션
- 시간 복잡도: O(n^2) |  공간 복잡도: O(n)
- 접근 방법
    - bfs 를 이용해 주어진 조건을 구현하면 됩니다
    - 시간초과로 pyp3 로 제출했습니다
<br/><br/>
* 풀이
  * bfs 로 모든 국가를 확인한다 ( 연합국가인지 아닌지 확인 후 맞다면 이동인구 총합 // 이동국가 수)
  * 인구의 이동이 있는지 flag 를 두어 cnt +1
<br/><br/>
- 코드
```python
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
    
```
---

### 3) [백준 17144] (https://www.acmicpc.net/problem/17144)
- 문제 유형: 구현,시뮬레이션
- 시간 복잡도:  O(n^2)  |  공간 복잡도: O(n)
- 접근 방법
    - 인터넷에 여러 풀이를 찾아봤습니다
    - 시간초과로 pyp3 로 제출했습니다
<br/><br/>
* 풀이
  * 모든 곳을 방문하며 인접한 곳 + g//5 더하기, g-(g//5)*cnt
  * 공기 청정기가 위인 경우 반시계방향, 아래인 경우 시계방향으로 순환
<br/><br/>
- 코드
```python
r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치
cleaner = []
for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            cleaner.append((i, j))

# 미세먼지 확산
def diffusion():
    global room, cleaner
    temp = [[0]*c for _ in range(r)]
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(r):
        for j in range(c):
            if room[i][j]==0 or room[i][j]==-1: continue
            cnt = 0
            for x, y in move:
                cx = i+x
                cy = j+y
                if 0<=cx<r and 0<=cy<c and room[cx][cy]!= -1:
                    temp[cx][cy] += room[i][j]//5
                    cnt += 1
            temp[i][j] += room[i][j]-cnt*(room[i][j]//5)
    temp[cleaner[0][0]][cleaner[0][1]] = -1
    temp[cleaner[1][0]][cleaner[1][1]] = -1
    room = temp

# 공기청정기 작동
def clean(x, y, move):
    last = 0
    j = 0
    start = (x, y)
    x += move[0][0]
    y += move[0][1]
    while x != start[0] or y != start[1]:
        next = room[x][y]
        room[x][y] = last
        last = next
        x += move[j][0]
        y += move[j][1]
        if not (0<=x<r and 0<=y<c):
            if j == 3: break
            x = x - move[j][0] + move[j+1][0]
            y = y - move[j][1] + move[j+1][1]
            j += 1

for _ in range(t):
    diffusion()
    clean(cleaner[0][0], cleaner[0][1], [(0, 1), (-1, 0), (0, -1), (1, 0)])
    clean(cleaner[1][0], cleaner[1][1], [(0, 1), (1, 0), (0, -1), (-1, 0)])
answer = 0
for i in range(r):
    for j in range(c):
        if room[i][j] and room[i][j] != -1:
            answer+= room[i][j]
print(answer)
```

