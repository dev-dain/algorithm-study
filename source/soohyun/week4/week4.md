## 4주차 공통문제
### [백준 14500 테트로미노](https://www.acmicpc.net/problem/14500)
- 문제 유형: 구현, 완전탐색
- 시간 복잡도: O(NM)
- 공간 복잡도: O(NM)
- 접근 방법
    - 감시문제처럼 가능한 경우를 모두 저장한 리스트를 만들어두고 완전탐색하면 되지 않을까 생각했다.
    - 근데 생각해보니.. 이렇게 하면 경우의 수가 너무 많을 뿐더러 내 머리가 정확하지 않을 것 같았다.
    - dfs와 완전탐색으로 풀면 되겠다까지는 생각했지만 도형을 놓는 경우를 어떻게 처리할지 생각나지 않았다.
    - 아이디어는 힌트를 보았고, 정사각형을 4개까지 놓으면 테트로미노를 만들 수 있다는 사실을 알았다.
    - 이를 기반으로 코드를 짰지만 시간 초과가 났는데, 그 이유는 가능성이 없는 경우는 제외를 시켜야되기 때문이다. (현재 탐색을 끝까지 해봤자 합의 최대값을 갱신할 수 없는 경우!)
    - 시간초과를 해결했지만 코드는 틀렸는데, 그 이유는 도형이 ㅗ인 경우를 따로 처리해줘야되기 때문이다.
    - 따로 추가 조건을 더 생각해야 하는 문제라서 어려웠던 것 같다.
<br/><br/>
- 풀이
    1. 방향벡터와 방문리스트 등 필요한 변수를 생성한다.
    2. DFS를 통해 테트로미노를 놓는 모든 경우의 수를 탐색한다.
        - 방문 처리를 하고 DFS 탐색을 한 후 방문 초기화를 꼭! 해줘야 된다.
    3. 끝까지 탐색을 해봤자 현재 합의 최대값(ans)을 갱신할 수 없는 경우에는 탐색을 그만둔다 (이 부분이 없으면 시간초과!)
    4. 테트로미노를 다 놓았다면(= 놓인 정사각형이 4개인 경우) 합의 최대값(ans)를 갱신한다.
    5. 네방향으로 다음에 놓일 정사각형 위치를 확인한다.
        - 다음 정사각형 위치가 범위를 벗어나지 않으며 아직 방문하지 않은 경우 정사각형을 놓는다
        - 이 때, 테트로미노가 ㅗ인 경우를 따로 처리해준다. (튀어나온 모양을 만들어주기 위해 방문처리는 하고 위치는 이동하지 않는다!)
    6. 모든 탐색이 끝나면 결과를 출력한다.
<br/><br/>
- 코드
```python
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
```

### [백준 16234 인구 이동](https://www.acmicpc.net/problem/16234)
- 문제 유형: 구현, 그래프
- 시간 복잡도: ...? O(V^2)
- 공간 복잡도: O(N^2)
- 접근 방법
    - 조건을 통해 인구이동이 가능한 나라만 큐에 삽입하여 BFS로 해결하면 되겠다고 생각했다.
    - 인구이동이 가능한 나라를 모두 구한 뒤에 인구 수를 갱신해줘야 됐다.
    - 연합한 나라 수를 세어서 인구 이동을 계속할 수 있는지 확인하는 과정이 필요했다.
<br/><br/>
- 풀이
    1. 반복문을 통해 인구이동이 불가능할 때까지 BFS를 통해 인구이동을 계속 한다.
    2. 시작노드를 큐에 삽입하고 방문처리를 한다. 그리고 필요한 정보를 저장할 변수를 생성한다.
    3. 큐에서 현재 나라 정보를 가져온 후, 연합한 나라에 추가한다.
    4. 현재 나라의 동서남북 방향으로 인구 차이가 L이상 R이하인 나라를 큐에 추가한다.
    5. 연합한 나라를 모두 구한 뒤, 인구 이동을 계속 할 수 있는지 확인한다.
        - 나라수가 1이면 인구이동이 불가능한 것이므로 return False
        - 아니라면, 인구이동이 가능한 것이므로 인구수를 갱신해준 뒤 return True
    6. 인구이동을 멈추지 않아도 된다면 횟수에 +1
    7. 인구이동을 멈춰야 한다면 반복문을 빠져나와 결과를 출력한다.
<br/><br/>
- 코드
```python
from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0] # 동서남북
answer = 0 # 인구 이동 횟수

def bfs(i, j):
    queue = deque([[i, j]])
    move = deque() # 연합한 나라
    visited[i][j] = 1
    cnt, people = 0, 0 # 연합한 나라수, 인구수

    while queue:
        x, y = queue.popleft()
        move.append([x, y])
        cnt += 1
        people += graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]: # 범위 내에 있으며 아직 방문하지 않은 경우
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R: # 인구수 차이가 L이상 R이하라면 연합에 추가
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
    
    # 인구이동이 불가능한 경우
    if cnt == 1:
        return False

    # 인구이동이 가능한 경우
    new = people // cnt
    while move:
        x, y = move.popleft()
        graph[x][y] = new
    return True


while True:
    visited = [[0] * N for _ in range(N)]
    stop = True # 인구이동을 멈출지 여부

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j): # 인구이동이 가능하다면 멈추지 않는다
                    stop = False

    if stop:
        break
    else:
        answer += 1

print(answer)
```

### [백준 17144 미세먼지 안녕!](https://www.acmicpc.net/problem/17144)
- 문제 유형: 구현, 시뮬레이션
- 시간 복잡도: ...? O(4RC + RC)
- 공간 복잡도: O(RC)
- 접근 방법
    - 처음엔 전체를 탐색하면서 미세먼지인 경우 바로 미세먼지가 확산되도록 코드를 짰다.
    - 이렇게 했더니 확산되는 값이 누적되어서 결과가 제대로 나오지 않았다.
    - 모든 미세먼지가 1초동안 동시에 확산되는 것이므로 전체를 돌면서 확산되는 양을 파악한 후, 마지막에 한번에 확산되는 양으로 변경시켜주었다.
    - 미세먼지를 이동시켜주는 것은 아이디어가 생각나지 않아 참고했다. 방향벡터를 쓰면 된다는 것을 알고 코드를 짰더니 해결할 수 있었다.
<br/><br/>
- 풀이
    1. 먼저 청소기의 위치를 구해 cleaner에 저장한다.
    2. 미세먼지를 확산시킨다.
        - 전체를 탐색하여 미세먼지인 경우 인접한 네방향을 확인한다.
        - 인접한 곳이 범위를 벗어나지 않으며 청소기가 아닌 경우 확산될 미세먼지 양을 구한다.
        - 확산될 미세먼지 양을 모두 구한 후, 확산되는 양만큼 변경시켜준다.
    3. 위쪽 -> 아래쪽 순서로 미세먼지를 이동시킨다.
        - 청소기 방향 순서대로 이동시키는데, 범위를 벗어나면 다음 방향으로 넘어간다.
        - 현재 위치가 청소기 위치와 같다면 이동을 멈춘다.
    4. 확산과 이동이 끝나면 최종 미세먼지 양을 계산한 후 출력한다.

<br/><br/>
- 코드
```python
import copy

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
cleaner = [] # 청소기 위치
answer = 0 # 최종 미세먼지 양

# 청소기 위치 구하기
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            cleaner.append([i, j])

# 미세먼지 확산하기
def diff():
    dust = [[0] * C for _ in range(R)] # 확산되는 미세먼지 양

    for x in range(R):
        for y in range(C):
            if graph[x][y] > 0: # 미세먼지인 경우
                d = graph[x][y] // 5 # 확산되는 양
                # 인접한 네방향 확인
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 범위를 벗어나지 않으며 청소기가 아닌 경우 확산될 미세먼지 양을 구한다
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                            dust[nx][ny] += d
                            dust[x][y] -= d

    # 확산되는 미세먼지 양으로 변경시킨다
    for i in range(R):
        for j in range(C):
            graph[i][j] += dust[i][j]

# 미세먼지 이동하기
def move(x, y, dir):
    temp = copy.deepcopy(graph)
    cx, cy = x, y
    temp[x][y] = 0 # 청소기 위치는 0으로

    # 청소기 이동 방향대로 이동시킨다
    for i in range(4):
        while True:
            nx = x + dx[dir[i]]
            ny = y + dy[dir[i]]
            if nx == cx and ny == cy: # 청소기 위치라면 이동을 멈춘다
                return
            if nx < 0 or nx >= R or ny < 0 or ny >= C: # 범위를 벗어나면 다음 방향으로 넘어간다
                break
            graph[nx][ny] = temp[x][y]
            x, y = nx, ny # 다음 칸으로 이동


# T초 동안 확산 -> 이동
for _ in range(T):
    diff()
    move(cleaner[0][0], cleaner[0][1], [1, 0, 3, 2])
    move(cleaner[1][0], cleaner[1][1], [1, 2, 3, 0])

for i in range(R):
    for j in range(C):
        if graph[i][j] != -1:
            answer += graph[i][j]
print(answer)
```