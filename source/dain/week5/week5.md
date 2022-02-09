## 5주 공통 문제 1
* 🥇❓ [백준 2573 빙산](https://www.acmicpc.net/problem/2573)

* 접근 방법
	* 제일 쉬워 보였지만 오히려 쩔쩔맨 문제
  * BFS/DFS 둘 모두로 풀 수 있는 문제(라고 생각했지만 시간 초과 안 나려면 결국 BFS로 푸는 문제)
  * 처음 생각은, 각 빙산 위치마다 녹는 개수를 세 준 다음 1년이 끝나는 시점마다 빙산이 분리되는지 확인하는 것이었음
    * (1) 빙산이 있으면 거기서 방향 벡터로 상하좌우에 바다가 얼마나 있는지 확인, melt를 업데이트함
    * (2) melt를 돌리면서 빙산을 실제로 녹임
    * (3) 빙산이 나눠져 있는지 확인
    * 즉 전체 맵을 2번 돌아야 했음
  * BFS로도 써 보고 DFS로도 써 봤지만 Python3로 제출하면 시간 초과, Pypy3로 제출하면 메모리 초과...
  * 뭐가 문젠지 알아보기 위해 정답 코드를 봄  
    
* 정리된 접근 방법
  * BFS로 하되, 녹는 개수를 세 주면서 빙산 개수를 1번에 세는 것으로 바꿔 줌
  * (1) 빙산을 보면 BFS 호출. 여기서 이어진 빙산을 쭉 둘러보며 바다와 얼마나 면해 있는지 한 번에 체크하면서 방문 확인함
  * (2) 즉, 방문 확인되지 않은 빙산에만 BFS를 호출하게 되는데 그러면 이 횟수가 곧 쪼개진 빙산 개수가 됨
  * (3) 그 다음 빙산을 실제로 녹이고 BFS 호출 횟수를 확인함
---
* 시간, 메모리 초과 코드
```python
from collections import deque

N, M = map(int, input().split())
arctic = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
melt = []
year = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  qu = deque([[x, y]])
  visited[x][y] = 1

  while qu:
    x, y = qu.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if not arctic[nx][ny] or visited[nx][ny]:
        continue
      visited[nx][ny] = 1
      qu.append([nx, ny])

while True:
  visited = [[0 for _ in range(M)] for _ in range(N)]
  for x in range(N):
    for y in range(M):
      cnt = 0
      if not arctic[x][y]:
        continue
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
          continue
        if not arctic[nx][ny]:
          cnt += 1
      melt.append([x, y, cnt])

  visited = [[0 for _ in range(M)] for _ in range(N)]
  location = []
  for x, y, cnt in melt:
    arctic[x][y] -= cnt
    if arctic[x][y] < 0:
      arctic[x][y] = 0
    if arctic[x][y]:
      location.append((x, y))
  year += 1
  land = 0
  for x, y in location:
    if not visited[x][y]:
      bfs(x, y)
      visited[x][y] = 1
      land += 1
  if not land:
    year = 0
    break
  if land > 1:
    break
print(year)
```
```python
from collections import deque

N, M = map(int, input().split())
arctic = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
melt = [[0 for _ in range(M)] for _ in range(N)]
year = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  qu = deque([[x, y]])
  visited[x][y] = 1

  while qu:
    x, y = qu.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if arctic[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = 1
        qu.append([nx, ny])
      elif not arctic[nx][ny]:
        melt[x][y] += 1

while True:
  visited = [[0 for _ in range(M)] for _ in range(N)]
  melt = [[0 for _ in range(M)] for _ in range(N)]
  cnt = 0
  for x in range(N):
    for y in range(M):
      if arctic[x][y] and not visited[x][y]:
        bfs(x, y)
        cnt += 1

  for x in range(N):
    for y in range(M):
      arctic[x][y] -= melt[x][y]
      if arctic[x][y] < 0:
        arctic[x][y] = 0

  if not cnt:
    year = 0
    break
  if cnt > 1:
    break
  year += 1
print(year)
```
- 시간복잡도 : O(N x M)
- 공간복잡도 : O(N x M)
- 문제 유형 : 그래프 (BFS/DFS), 시뮬레이션
- Pypy3 제출, 228784KB / 940ms
---
---
## 5주 공통 문제 2
* 🥇 [백준 11559 Puyo Puyo](https://www.acmicpc.net/problem/11559)
* 접근 방법
	* 중간 난이도처럼 느껴졌는데 실제로 풀어 보니 제일 쉬웠음
  * 다만 문제는 동시에 터지는 것들을 어떻게 같이 처리하는가임 (동시에 터지는 것을 1회로 친다는 점에서, 이 문제는 인구 이동 문제와 비슷하게 생각할 수 있음)
  * 인구 이동처럼 터지는 뿌요들의 위치를 저장해두는 큰 리스트를 관리하면 됨
  * 12 * 6으로 크기는 픽스되어 완탐해도 딱히 큰 부담은 없어보임
  * (1) 12줄을 차례대로 돌되, .으로 전부 채워진 빈 줄은 앞으로도 다른 색깔로 채워질 일이 없으므로 다음 루프에서 볼 필요 없다는 표시를 해줌
  * (2) 글자가 있다면 BFS를 돌기 시작함. 같은 글자가 얼마나 붙어 있는지 세고 4개가 안 되면 버림
  * (3) 4개 이상이 된다고 해도 전체 필드를 다 보기 전까지는 터뜨리면 안 되므로 큰 리스트에 저장함
  * (4) 필드를 다 돌면 리스트에 있는 것들을 터뜨리기 시작함. 터뜨리는 건 위에 있는 걸 그냥 복사해서 원 위치에 있는 것을 없애버리는 것으로 대신함 (대신, 0번 줄이 터지면 '.'으로 대체함)
  * (5) 큰 리스트에 아무것도 없을 때까지 (1)~(4)번 반복
---
* 정답 코드
```python
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
location = []
visited = [[0 for _ in range(6)] for _ in range(12)]
def bfs(color, x, y):
  qu = deque([[x, y]])
  delete = [[x, y]]

  while qu:
    x, y = qu.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
        continue
      if field[nx][ny] != color or visited[nx][ny]:
        continue
      visited[nx][ny] = 1
      qu.append([nx, ny])
      if [nx, ny] not in delete:
        delete.append([nx, ny])
  return [] if len(delete) < 4 else delete

field = [list(input()) for _ in range(12)]
d_row = 0
combo = 0
while True:
  d = []
  location = []
  visited = [[0 for _ in range(6)] for _ in range(12)]
  add = 0
  for i in range(d_row, 12):
    if field[i] == ['.', '.', '.', '.', '.', '.',]:
      d_row += 1
      visited[i] = [1, 1, 1, 1, 1, 1]
      continue

    for j in range(6):
      if field[i][j] == '.' or visited[i][j] or [i, j] in location:
        continue
      color = field[i][j]
      visited[i][j] = 1
      delete = bfs(color, i, j)
      if not delete:
        continue
      d.append(delete)
      location += delete
  
  if not d:
    break
  
  for delete in d:
    for x, y in delete:
      if x == 0:
        field[x][y] = '.'
        continue
      while field[x][y] != '.' and x > 0:
        field[x][y] = field[x-1][y]
        x -= 1
      field[0][y] = '.'
  
  combo += 1
print(combo)
```
- 시간복잡도 : O(V+E), 전체 순회 자체는 O(1)
- 공간복잡도 : O(1)
- 문제 유형 : BFS, 구현, 시뮬레이션
- Python3 제출, 32480KB / 88ms

## 5주 공통 문제 3
* 🥇 [백준 20056 마법사 상어와 파이어볼](https://www.acmicpc.net/problem/20056)
  
* 접근 방법
	* 이 문제가 제일 어려웠음 (일단 독해하는 것 자체가 챌린지였음.. 실제로 문제 잘못 읽어서 엄청 길게 풀음)
  * 미세먼지 안녕! 문제와 흡사. 단 이 경우에는 8방향 벡터를 써야 하고, 1번-N번 행이 연결되어 있다는 것을 계산해야 함. 즉, 경계를 벗어나도 없어지는 게 아니라 반대편으로 넘어가는 것임
  * 사실 그렇게.. 어려운 문제는 아닌데 문제를 잘못 읽어서 한참 못 풀음
  * 중요한 건 맵에 배치를 하는 게 아니라 마지막에 남은 파이어볼량의 질량이기 때문에 맵에 표시하는 것 자체는 중요하지 않음. 분리되는 파이어볼을 일일이 맵에 표시하지 않고 일단 파이어볼에 저장하는 게 중요
  * (1) 입력으로 들어오는 파이어볼을 파이어볼 리스트에 저장. 이 때, 맵에 실제 배치하지는 않음
  * (2) 1번 이동을 시킨 다음, 파이어볼 리스트를 비워줌. 
  * (3) 전체 맵을 돌면서 파이어볼이 있는 좌표를 찾음. 이 때, 한 개만 있으면 단순히 파이어볼 리스트에 넣고 지나감
  * (4) 만약 파이어볼이 2개 이상이라면 질량, 속력을 합쳐 나눠두고, 전체 파이어볼의 방향을 계산해 4개 파이어볼이 갈 방향을 각각 지정함
  * (5) (2)~(4)번을 K번 동안 반복함
  
---
* 정답 코드
```python
N, M, K = map(int, input().split())
board = [[[] for _ in range(N+1)] for _ in range(N+1)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
fireball = []
for _ in range(M):
  r, c, m, s, d = map(int, input().split())
  fireball.append([r, c, m, s, d])
for _ in range(K):
  for i in range(len(fireball)):
    r, c, m, s, d = fireball[i]
    nx, ny = r, c
    for _ in range(s):
      nx = nx + dx[d]
      ny = ny + dy[d]
      if nx < 1:
        nx = N
      elif nx > N:
        nx = 1
      if ny < 1:
        ny = N
      elif ny > N:
        ny = 1
    board[nx][ny].append([m, s, d])
  fireball = []

  for i in range(1, N+1):
    for j in range(1, N+1):
      if not len(board[i][j]):
        continue
      if len(board[i][j]) == 1:
        # fireball.append([i, j] + board[i][j])
        # board[i][j]가 리스트일 때, pop을 하면 리스트 요소가 차례대로 나오지만 board[i][j]를 하면 그냥 리스트 자체가 나옴
        # 그래서 잘못된 리스트가 만들어짐에 주의
        fireball.append([i, j] + board[i][j].pop())
        continue
      mass = 0
      speed = 0
      direct = board[i][j][0][2] % 2
      flag = True
      for m, s, d in board[i][j]:
        mass += m
        speed += s
        if not flag:
          continue
        if d % 2 != direct:
          flag = False
      s_m = mass // 5
      s_s = speed // len(board[i][j])
      board[i][j] = []

      if s_m == 0:
        continue
      for x in range(4):
        s_d = (x * 2)
        if not flag:
          s_d += 1
        # 왜 nx, ny가 아니라 i, j지? 이해가 안된다
        # 아....!!! 바로 움직이는 게 아니라 분산은 나중에 시키는거구나..
        # 미쳤군.. 이게 문맹이지..
        fireball.append([i, j, s_m, s_s, s_d])
print(sum([ball[2] for ball in fireball]))
```
- 시간복잡도 : O(K * N^2)
- 공간복잡도 : O(N^2)
- 문제 유형 : 구현, 시뮬레이션
- Pypy3 제출, 145168KB / 1124ms