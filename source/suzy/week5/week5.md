## 5주차
### 1) [백준 2573] (https://www.acmicpc.net/problem/2573)
- 문제 유형: 그래프, 구현
- 시간 복잡도: O(n*m)  |  공간 복잡도: O(n)
- 접근 방법
    - 동서남북 네 방향을 확인하며 존재하는 0의 칸수만큼 빼주고 0보다 작거나 0이 되는 경우 높이는 0 으로 .. 
    - bfs 를다시 호출하는 경우가 분리된 경우
<br/><br/>
* 풀이
  * pyp3 로 제출했습니다
  * bfs 를 돌며 0 인 경우를 저장하고 빙산을 깎습니다
  * 빙산이 분리될 때까지 반복하며 result 리스트의 길이를 통해 분리된 경우 day +1 합니다
<br/><br/>
- 코드
```python
from collections import deque
import sys
input = sys.stdin.readline
# 세로 가로
n, m = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(n)]

# 동서남북
dx = [1,-1,0,0]
dy = [0,0,-1,1]

day = 0
check = False

# bfs
def bfs(i,j):
    q = deque()
    q.append((i,j))
    
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] !=0 and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

# 빙산이 분리될 때까지 반복
while True:
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))
                
    # 빙산 깎기
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    # 다 녹을때까지 분리되지 않으면
    if len(result) == 0:
        break
    # 빙산이 분리되면
    if len(result) >=2:
        check = True
        break
    day += 1
    
if check:
    print(day)
else:
    print(0)
```
---

### 2) [백준 11559] (https://www.acmicpc.net/problem/11559)
- 문제 유형: 구현, 그래프, 시뮬레이션
- 시간 복잡도: O(n*m) |  공간 복잡도: O(n)
- 접근 방법
    - 같은 색깔인 경우 제거해주는 방법과 뿌요가 터졌을때 다시 위치를 재정렬해주어야합니다.
    - 시간초과로 pyp3 로 제출했습니다
<br/><br/>
* 풀이
  * bfs 로 상하좌우를 확인하며 같은 색깔인 경우를 확인하고 새로 터지는 뿌요가 없을때까지 반복합니다
  * down 함수를 통해서는 위로 올라가며 뿌요의 위치를 재정렬합니다 
<br/><br/>
- 코드
```python
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    for d in range(4):	# 상하좌우
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < 12 and 0 <= Y < 6:
            # 같은 색깔인 경우
            if board[X][Y] == board[x][y] and visited[X][Y] == 0:
                q.append([X, Y])
                visited[X][Y] = 1

def down():
    for y in range(6):
        tmp = deque([])
        for x in range(11, -1, -1):
            # 뿌요 위치 저장
            if board[x][y] != '.':
                tmp.append(board[x][y])
        for x in range(11, -1, -1):
            if tmp:	# 뿌요를 하나씩 꺼내어 보드에 기록
                board[x][y] = tmp.popleft()
            else:	# 비면 뿌요 없음
                board[x][y] = '.'

board = []
for _ in range(12):
    board.append(list(input()))

chk = 0
answer = 0
while True:		# 새로 터지는 뿌요가 없을 때까지 반복
    visited = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                q = deque([[i, j]])                
                stack = []	# 뿌요 위치를 기록할 스택
                while q:
                    now = q.popleft()
                    stack.append(now)
                    bfs(now[0], now[1])
                if len(stack) >= 4:	# 이어진 뿌요가 4개 이상일 때
                    chk = 1
                    for s in stack:
                        board[s[0]][s[1]] = '.'	# 뿌요 터진경우
    down()
    if chk == 0:
        break
    chk = 0
    answer += 1
print(answer)
```
---

### 3) [백준 20056] (https://www.acmicpc.net/problem/20056)
- 문제 유형: 구현, 시뮬레이션
- 시간 복잡도:  O(N^2)  |  공간 복잡도: O(N)
- 접근 방법
    - 문제 이해가 안되서 풀이를 찾아보았습니다 ..
    - r,c,m,s,d 위치와 질량 속력 방향이 주어지면 방향만큼 속력으로 이동합니다
    - 같은 파이어볼이 존재할경우 4개로 나누고 주어진 조건으로 나누어 줍니다
<br/><br/>
* 풀이
  * k 번 이동 횟수만큼 조건을 돌며 2개 이상의 파이어볼이 존재할 경우 모두 합하고 4개로 나누어줍니다
  * 모두 홀수이거나 짝수인 경우와 그외의 경우를 구하여 이동방향을 정해줍니다
  * 리스트에서 질량의 합을 구해 출력합니다
<br/><br/>
- 코드
```python
N,M,K = map(int, input().split())
# r,c,m,s,d
fire = []
for _ in range(M):
    _r,_c,_m,_s,_d = list(map(int, input().split()))
    fire.append([_r-1,_c-1,_m,_s,_d])

graph = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

# 파이어볼 이동
for _ in range(K):
    while fire:
        cr,cc,cm,cs,cd = fire.pop()
        # 1번과 N 행이 연결되어 있기 때문
        nr = (cr + cs * dx[cd]) % N
        nc = (cc + cs * dy[cd]) % N
        graph[nr][nc].append([cm,cs,cd])
        
    # 2개 이상인지 확인
    for r in range(N):
        for c in range(N):
            # 2개 이상인 경우 > 4 로 쪼개기
            if len(graph[r][c]) > 1:
                summ,sums,cnt_odd, cnt_even, cnt = 0,0,0,0,len(graph[r][c])
                while graph[r][c]:
                    _m,_s,_d = graph[r][c].pop()
                    summ += _m
                    sums += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                # 모두 홀수이거나 짝수인 경우
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]
                # 질량이 0이면 소멸
                if summ // 5:
                    for d in nd:
                        fire.append([r,c,summ//5,sums//cnt, d])
                        
            # 1개인 경우
            if len(graph[r][c]) == 1:
                fire.append([r,c]+ graph[r][c].pop())
                
print(sum([i[2] for i in fire]))
```

