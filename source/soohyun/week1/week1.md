## 1주차 개별문제
### [백준 14502 연구소](https://www.acmicpc.net/problem/14502)
- 문제 유형: 그래프, 완전탐색
- 시간 복잡도: O(N^2)
- 공간 복잡도: O(N)
- 접근 방법
    - 벽을 3개 세우는 경우마다 안전영역의 크기를 구해야 안전영역의 최대값을 구할 수 있다.
    - 따라서 벽을 3개 세우는 모든 경우를 구해야 한다.
    - 벽을 3개 세웠다면 안전영역의 크기를 구하면 되는데, 이 때 "바이러스의 위치"를 먼저 구한다 -> 안전영역의 크기를 구하는 시간을 줄일 수 있다!
    - 퍼지거나 감염되는 문제인 경우 미리 위치를 구하고 탐색하는 것이 좋다.
<br/><br/>
- 풀이
    1. 벽을 세울 수 있는 모든 경우를 탐색한다. (완전탐색)
        - 벽이 3개 미만이라면 빈칸에 벽을 세운다. (모든 경우를 탐색해야 하므로 꼭 초기화!!)
        - 벽이 3개 세워지면 바이러스를 퍼지게 한다.
     2. 바이러스를 퍼지게 하여 안전영역의 크기를 구한다. (BFS)
        - 먼저 바이러스의 위치를 큐에 삽입한다.
        - 범위 안에 있거나 빈칸인 경우 바이러스를 퍼지게 한다.
        - 안전영역의 최대 크기를 구한다.
    3. 모든 경우의 탐색이 끝나면 결과를 출력한다.
<br/><br/>
- 코드
```python
from collections import deque
import copy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
answer = 0 # 안전영역 크기의 최대값

# 벽 세우기
def wall(w):
    if w == 3: # 벽이 3개 세워지면 바이러스를 퍼지게 한다
        bfs()
        return

    # 벽이 3개 미만이라면 벽을 세운다
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(w+1)
                graph[i][j] = 0 # 초기화

# 바이러스 퍼지게 한 후 안전영역 크기 구하기
def bfs():
    global answer
    g = copy.deepcopy(graph)
    queue = deque()
    
    # 바이러스 위치를 큐에 삽입
    for i in range(N):
        for j in range(M):
            if g[i][j] == 2:
                queue.append([i, j])

    # 바이러스를 퍼지게한다
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if g[nx][ny] == 0:
                    queue.append([nx, ny])
                    g[nx][ny] = 2

    # 안전영역 크기의 최대값을 구한다
    count = 0
    for x in g:
        count += x.count(0)
    answer = max(answer, count)

wall(0) # 벽을 세운 후 바이러스를 퍼지게 하여 안전 영역의 최대값을 구한다
print(answer)
```

### [백준 14503 로봇 청소기](https://www.acmicpc.net/problem/14503)
- 문제 유형: 구현, 시뮬레이션
- 시간 복잡도: O(N^2)
- 공간 복잡도: O(1)
- 접근 방법
    - 바라보고 있는 방향에 따른 위치 이동을 해주는 것이 중요!
    - 나머지는 문제에 제시된대로 구현만 하면 된다.
    - 하지만 구현하는 것이 어려워서 풀이를 찾아보았다. 다양한 풀이가 있었는데 가장 이해하기 쉬운 풀이로 가져왔다.
<br/><br/>
- 풀이
    1. 방향 벡터를 생성한다. 문제에서 제시된 바라보는 방향에 맞게 "북동남서" 순으로!
    2. 현재 위치에서 로봇 청소기가 작동한다.
    3. 현재 위치를 청소한다 -> 청소한 칸은 2로 만들어주고, 청소한 칸의 개수에 +1 (조건 1)
    4. 네 방향을 확인한다. (조건 2)
        - 왼쪽 방향과 왼쪽 방향의 위치를 구한다.
        - 청소 범위이며 아직 청소하지 않았다면 전진한다. -> 2번부터 다시 진행 (조건 2-a)
        - 청소했다면 방향을 변경한다. (조건 2-b)
    5. 네 방향 모두 이동할 수 없다면 후진할 위치를 구한다.
        - 후진할 위치가 벽이라면 작동을 멈춘다. (조건 2-d)
        - 후진할 수 있다면 방향을 유지한 채 위치를 변경한다. (조건 2-c)
    6. 로봇 청소기 작동이 종료되면 청소한 칸의 개수를 출력한다.
<br/><br/>
- 코드
```python
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
```