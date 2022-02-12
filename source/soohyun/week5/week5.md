## 5주차 공통문제
### [백준 2573 빙산](https://www.acmicpc.net/problem/2573)
- 문제 유형: 구현, 그래프
- 시간 복잡도: O(NM)
- 공간 복잡도: O(NM)
- 접근 방법
    - 단순 구현 문제로 먼저 빙산을 녹인 다음 빙산 덩어리 개수를 세면 되겠다고 생각했다.
    - 시간초과가 나서 다시 문제를 읽어보니 '빙산이 다 녹을 때까지 분리되지 않으면 0을 출력' 조건을 넣어주지 않았다. 문제를 잘 읽어야겠다...
    - 이 조건을 추가해도 시간초과가 나서 PyPy로 제출했더니 통과되었다.
<br/><br/>
- 풀이
    1. 빙산을 녹인다.
        - 빙산의 녹은 높이를 저장할 height 리스트를 생성한다.
        - 빙산의 녹은 높이를 구한 후, 녹은 높이만큼 빙산 높이를 변경한다.
        - 이 때, 높이는 0보다 줄어들 수 없으므로 체크해줘야 한다.
    2. 빙산의 덩어리 개수를 센다.
        - BFS를 사용해서 빙산의 덩어리 개수를 구한다.
    3. 덩어리 개수가 0이라면 더 이상 녹을 빙산이 없는 것이므로 flag = True를 하고 멈춘다.
    4. 덩어리 개수가 2이상 이라면 멈추고 결과를 출력한다.
<br/><br/>
- 코드
```python
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
ans = 0 # 빙산이 분리되는 시간
flag = False # 빙산이 분리되는지 체크

# 빙산 녹이기
def melt():
    height = [[0] * M for _ in range(N)] # 빙산의 녹은 높이

    # 빙산의 녹은 높이 구하기
    for x in range(N):
        for y in range(M):
            if graph[x][y] != 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                        height[x][y] -= 1

    # 녹은 높이만큼 빙산 높이 변경
    for x in range(N):
        for y in range(M):
            if graph[x][y] + height[x][y] < 0: # 높이는 0보다 더 줄어들 수 없다
                graph[x][y] = 0
            else:
                graph[x][y] += height[x][y]

# 빙산 덩어리 구하기
def bfs(i, j):
    queue = deque([[i, j]])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] != 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

while True:
    melt() # 빙산 녹이기

    cnt = 0
    visited = [[0] * M for _ in range(N)]

    # 빙산 덩어리 구하기
    for x in range(N):
        for y in range(M):
            if not visited[x][y] and graph[x][y] != 0:
                bfs(x, y)
                cnt += 1

    ans += 1

    if cnt == 0: # 빙산이 다 녹을 때까지 분리되지 않는 경우
        flag = True
        break

    if cnt >= 2: # 빙산의 덩어리가 2이상인 경우
        break

print(0) if flag else print(ans)
```

### [백준 11559 Puyo Puyo](https://www.acmicpc.net/problem/11559)
- 문제 유형: 구현, 그래프
- 시간 복잡도: O(NM)
- 공간 복잡도: O(NM)
- 접근 방법
    - 4개 이상의 뿌요를 없앤 뒤에 뿌요를 아래로 옮기면 되겠다고 생각했다.
    - 하지만 뿌요를 아래로 옮기는 함수가 오래걸려서 시간초과가 났다.
    - 어떻게 시간초과를 해결해야할지 모르겠어서 뿌요를 아래로 옮기는 것은 다른 사람 풀이를 참고했다.
    - 이 부분을 해결했는데도 시간초과가 나서 이유를 찾는데 애를 먹었는데...
    - 터트릴 뿌요가 있을 때만 flag = False를 했어야 했는데 bfs를 수행할 수 있을 때 모두 flag = False를 해서 시간초과가 난 것이었다...
<br/><br/>
- 풀이
    1. 뿌요를 없앤다.
        - 터트릴 수 있는 뿌요를 저장할 puyo 리스트를 생성한다.
        - 같은 색깔의 뿌요라면 큐와 puyo에 삽입한다.
        - 같은 색깔의 뿌요가 4개 이상이라면 없앤 후 개수를 리턴한다.
    2. 터트릴 뿌요가 있다면 flag = False를 만들어준다.
    3. 터트릴 뿌요가 없다면 멈춘다.
    4. 뿌요를 아래로 떨어뜨린다.
        - 뿌요를 아래부터 탐색하면서 아래로 떨어뜨릴 수 있는 경우에 뿌요를 옮긴다.
    5. 결과를 출력한다.
<br/><br/>
- 코드
```python
from collections import deque
import sys

input = sys.stdin.readline
graph = [list(input()) for _ in range(12)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
ans = 0 # 연쇄 횟수

# 뿌요 없애기
def bfs(i, j, state):
    queue = deque([[i, j]])
    puyo = [[i, j]] # 같은 색의 뿌요 리스트
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위에 있고 아직 방문하지 않은 뿌요이며 현재 뿌요와 색깔이 같은 경우
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and graph[nx][ny] == state:
                queue.append([nx, ny])
                puyo.append([nx, ny])
                visited[nx][ny] = 1

    # 같은 색의 뿌요가 4개 이상이면 없앤다
    if len(puyo) >= 4:
        for x, y in puyo:
            graph[x][y] = '.'
    
    return len(puyo)

# 뿌요가 아래로 떨어지기
def down():
    for j in range(6):
        for i in range(10, -1, -1):
            for k in range(11, i, -1):
                if graph[i][j] != '.' and graph[k][j] == '.':
                    graph[k][j] = graph[i][j]
                    graph[i][j] = '.'
                    break

while True:
    visited = [[0] * 6 for _ in range(12)]
    flag = True # 터트릴 뿌요가 없는지 체크

    # 뿌요 없애기
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and graph[i][j] != '.':
                if bfs(i, j, graph[i][j]) >= 4: # 터트릴 뿌요가 있다면 flag = False
                    flag = False

    if flag: break

    ans += 1
    down() # 뿌요 아래로 떨어지기

print(ans)
```

### [백준 20056 마법사 상어와 파이어볼](https://www.acmicpc.net/problem/20056)
- 문제 유형: 구현, 시뮬레이션
- 시간 복잡도: O(N^2 * K)
- 공간 복잡도: O(N^2)
- 접근 방법
    - 이 문제는 조건이 많아서 가장 어렵게 느껴졌던 문제였다.
    - 그대로 구현하기만 하면 되는데 코드로 옮기기가 어렵다...
    - 1-N번 행이 연결되어 있고, 1-N번 열이 연결되어 있다는 것이 처음에 이해가 잘 되지 않았다.
    - fireballs에 파이어볼 정보를 저장해두고 하나씩 꺼내면서 파이어볼을 이동시켰다.
<br/><br/>
- 풀이
    1. 파이어볼을 저장할 fireballs와 파이어볼이 발사된 격자인 graph를 생성한다.
    2. 파이어볼을 하나씩 꺼내서 이동시킨다.
        - 파이어볼이 이동할 위치를 구해 graph에 위치시킨다.
    3. graph를 탐색하여 이동 후 처리를 해준다.
        - 같은 칸에 파이어볼이 1개인 경우에는 fireballs에 삽입한다.
        - 같은 칸에 파이어볼이 여러개인 경우 질량합, 속력합, 방향의 짝수와 홀수 개수를 구한다.
        - 방향의 짝수와 홀수 개수에 따라 파이어볼이 이동할 방향을 지정한다.
        - 지정한 방향에 따른 파이어볼을 fireballs에 삽입한다. (이 때, 질량이 0이면 소멸)
    4. 남아 있는 파이어볼 질량 합을 출력한다.

<br/><br/>
- 코드
```python
from collections import deque

N, M, K = map(int, input().split())
fireballs = deque()
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

for _ in range(K):
    graph = [[deque() for _ in range(N)] for _ in range(N)]

    # 파이어볼 이동하기
    while fireballs:
        r, c, m, s, d = fireballs.popleft()
        nr = (r + s * dx[d]) % N # 1-N번 행 연결
        nc = (c + s * dy[d]) % N # 1-N번 열 연결
        graph[nr][nc].append([m, s, d])

    for r in range(N):
        for c in range(N):
            if len(graph[r][c]) > 1: # 같은 칸에 파이어볼이 여러 개인 경우
                sum_m, sum_s, even, odd, cnt = 0, 0, 0, 0, len(graph[r][c]) # 질량합, 속력합, 짝수개수, 홀수개수, 파이어볼 개수
                while graph[r][c]:
                    m, s, d = graph[r][c].popleft()
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0: even += 1
                    else: odd += 1
                
                if even == cnt or odd == cnt: nd = [0, 2, 4, 6] # 방향이 모두 홀수거나 짝수인 경우
                else: nd = [1, 3, 5, 7]

                if sum_m // 5 > 0: # 질량이 0이상 이라면 파이어볼 큐에 추가 (질량이 0이면 소멸)
                    for d in nd:
                        fireballs.append([r, c, sum_m // 5, sum_s // cnt, d])
            elif len(graph[r][c]) == 1: # 같은 칸에 파이어볼이 1개인 경우 -> 파이어볼 큐에 추가
                fireballs.append([r, c] + graph[r][c].popleft())

print(sum([f[2] for f in fireballs])) # 남아있는 파이어볼의 질량 합
```