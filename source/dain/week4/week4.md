## 4주 공통 문제 1
* 🥇❓ [백준 14500 테트로미노](https://www.acmicpc.net/problem/14500)

* 접근 방법
	* 직관적으로 생각해 보면 가능한 경우의 수를 모두 시도해서 구하면 될 것 같았음
  * 결국 완전탐색 문제의 대표격 되는 것이라고 생각해서 진짜 하나하나 다 구하기 시작(...)
  * 그래서 나온 경우의 수는 총 19가지. 
  * 이것을 종이 위에 올려보면서 테스트하기로 함
  * 일단 냅다 tetromino 경우의 수를 리스트에 담아준다. x, y 좌표값을 담아 만듦
  * 뭔가 더 좋은 방법이 있을 것 같아서 검색도 해봤는데 다른 풀이는 쉽게 이해되지는 않아서 이 방법을 채택
  * 이걸 적고 백트랙킹으로 푸신 분이 있는지 이제 코드를 볼 예정입니다 

---
* 정답 코드
```python
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
# 가로, 세로 좌표를 그냥 다 찍어버림
# 뭔가 이렇게 살면 안 될 것 같지만..
tetromino = [
  [(0, 0), (0, 1), (1, 0), (1, 1)],
  [(0, 0), (0, 1), (0, 2), (0, 3)],
  [(0, 0), (1, 0), (2, 0), (3, 0)],
  [(0, 0), (0, 1), (0, 2), (1, 0)],
  [(0, 0), (0, 1), (0, 2), (-1, 2)],
  [(0, 0), (1, 0), (1, 1), (1, 2)],
  [(0, 0), (0, 1), (0, 2), (1, 2)],
  [(0, 0), (1, 0), (2, 0), (2, 1)],
  [(0, 0), (0, 1), (1, 1), (2, 1)],
  [(0, 0), (0, 1), (1, 0), (2, 0)],
  [(0, 0), (1, 0), (2, 0), (2, -1)],
  [(0, 0), (1, 0), (1, 1), (2, 1)],
  [(0, 0), (0, 1), (1, 0), (-1, 1)],
  [(0, 0), (0, 1), (1, 0), (1, -1)],
  [(0, 0), (0, 1), (1, 1), (1, 2)],
  [(0, 0), (0, 1), (0, 2), (1, 1)],
  [(0, 0), (1, 0), (1, 1), (1, -1)],
  [(0, 0), (1, 0), (2, 0), (1, -1)],
  [(0, 0), (1, 0), (1, 1), (2, 0)]
]

res = []
# 그냥 단순히 모든 좌표를 돌면서 테트로미노를 테스트해봅니다
# 역시 이러면 안 될 것 같지만.. ^^
for i in range(N):
  for j in range(M):
    for t in tetromino:
      tmp = 0
      for x, y in t:
        try:
          tmp += paper[i + x][j + y]
        except:
          break
      else:
        res.append(tmp)
print(max(res))
```
- 시간복잡도 : O(N x M). 최대 250,000 * 19
- 공간복잡도 : O(N)
- 문제 유형 : 백트랙킹, 구현, 시뮬레이션
- Pypy3 제출, 224168KB / 524ms
---
---
## 4주 공통 문제 2
* 🥇 [백준 16234 인구 이동](https://www.acmicpc.net/problem/16234)
* 접근 방법
	* 개인적으로 공통 문제들 중에서 가장 까다로운 문제였다고 느껴지는 문제
  * BFS로 풀 수 있을 것 같았는데, 백트래킹 연습을 하려면 DFS로 푸는 연습을 해야 할 것 같아서 DFS로 풀어봄
    * 재귀가 깊지 않아서인지 재귀 깊이를 따로 설정해주지 않아도 에러가 나지는 않았음
  * 같은 연합이라는 것을 어떻게 정하고, 하루에 여러 연합이 있을 때 어떻게 묶어서 계산해야 할지 생각하는 게 까다로웠음

* 풀이
  * 바깥에서 무한루프를 돌리되 연합이 없으면 프로그램을 종료하는 식으로 구현
  * 무한루프 1회에서는 2중 for문으로 전체 나라를 돌음. 이 때, visited 처리가 안 된 방문 안 한 나라라면 dfs를 함
  * dfs의 결과를 연합을 이루는 나라의 개수 cnt와 연합국의 위치 좌표를 담은 리스트 country를 받음. 연합국이 만들어지지 않았다면 넘어감
  * 만약 연합국이 만들어졌다면 나라의 개수는 cnt_list에, 연합국 좌표 리스트는 하루의 연합국 리스트인 country_list에 추가함. 왜 추가하냐면 전체 땅을 다 돌아서 연합국의 위치와 개수를 전부 파악한 다음 마지막에 한꺼번에 처리해줘야 섞이는 오류 등이 생기지 않기 때문임
  * country_list에서 연합국들을 하나씩 빼내서 연합국 내의 인구 수를 더하고, 연합국 수로 나눠서 연합국 리스트에 배정한다
  * while 루프 1번에서 country_list 루프가 다 돌고 나면 하루에 일어날 인구 이동이 다 일어난 것이므로 day += 1을 해주고 끝
  * 이것을 연합국이 만들어지지 않을 때까지 반복
  
* 문제
  * 시간 초과 문제가 있었음. visited를 제대로 활용하지 못했기 때문에 일어난 문제였음
  * 시간 초과 코드에서는 while 루프 내에서 visited 표시를 했는데, 바꾼 코드에서는 dfs 내에서 연합국이 될 수 있는지 체크할 때 visited를 표시함. 그러고 나니까 시간 초과가 없어짐
  * while 루프 내에서 visited 표시를 하면 이미 연합국으로 속했을지라도 또 검사하게 되어 비효율적임
---
* 정답 코드
```python
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
day = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, visited, country, num, cnt):
  # 시간 초과를 없애준 코드
  visited[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
      continue
    if [nx, ny] in country:
      continue
    if L <= abs(land[x][y] - land[nx][ny]) <= R:
      country.append([nx, ny])
      cnt, country = dfs(nx, ny, visited, country, num, cnt + 1)
  return cnt, country

while True:
  visited = [[0 for _ in range(N)] for _ in range(N)]
  num = 1
  cnt = 0
  cnt_list = []
  country_list = []
  for i in range(N):
    for j in range(N):
#       시간 초과의 원인
#       visited[i][j] = 1
      if not visited[i][j]:
        visited[i][j] = 1
        cnt, country = dfs(i, j, visited, [[i, j]], num, 1)
        if cnt == 1:
          continue
        cnt_list.append(cnt)
        country_list.append(country)
        num += 1
  if num == 1:
    break
  for i in range(len(cnt_list)):
    people = 0
    for x, y in country_list[i]:
      people += land[x][y]
    people = people // cnt_list[i]
    for x, y in country_list[i]:
      land[x][y] = people
  day += 1
print(day)
```
- 시간복잡도 : O(N^2)
- 공간복잡도 : O(N^2)
- 문제 유형 : DFS, 시뮬레이션
- Pypy3 제출, 166412KB / 3520ms

## 4주 공통 문제 3
* 🥇 [백준 17144 미세먼지 안녕!](https://www.acmicpc.net/problem/17144)
  
* 접근 방법
	* 사실 이 문제가 세 문제 중 가장 무난하다는 생각이 들었음. 요구 조건이 그리 어렵지 않다
  * 단, 미세먼지가 확산할 때 확산량을 합쳐주면 에러가 나므로 확산한 후에 자기 위치에 남은 먼지와 확산되는 위치와 확산량을 따로 구분해주는 것이 포인트
  * 또, 공기청정기가 2칸인데 위쪽은 반시계, 아래쪽은 시계방향이므로 방향벡터를 거꾸로 잘 써먹는 것이 중요했음
  * 사실 시키는대로 구현하면 돼서 구현이 그렇게 어렵지는 않았음.
  * 미세먼지 위치와 공기청정기 위치 확보 -> 미세먼지가 퍼지는 좌표와 양을 확보하면서 동시에 미세먼지가 퍼진 다음 원래 먼지가 있던 좌표의 양 구하기 -> 미세먼지가 퍼지는 좌표에 양을 더해주기 -> 공기청정기 돌려주기 총 4단계로 나눠 코드를 구현
  * 공기청정기가 돌아가면서 칸이 한 칸씩 밀리는 게 오히려 구현하기 까다로웠는데 그냥 tmp 값에 이전 좌표의 값을 갖고 있다가, 바꿔야 할 때가 되면 해당 좌표의 값과 tmp를 서로 바꿔주면 됐음 
  
---
* 정답 코드
```python
R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
# 반시계방향으로 방향벡터 구성
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
machine = []

for _ in range(T):
  dust = []
  diffuse = []
  # 먼지 위치 확보
  for i in range(R):
    for j in range(C):
      if not room[i][j]:
        continue
      if room[i][j] == -1:
        machine.append([i, j])
        continue
      dust.append([i, j])

  # 먼지 확산 후 남은 양으로 갱신
  for x, y in dust:
    if room[x][y] < 5:
      continue
    cnt = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= R or ny < 0 or ny >= C:
        continue
      # 공기청정기 쪽으로는 확산 X
      if room[nx][ny] == -1:
        continue
      diffuse.append([nx, ny, room[x][y] // 5])
      cnt += 1
    room[x][y] = room[x][y] - ((room[x][y] // 5) * cnt)
  # 확산 먼지들의 좌표를 찾아 더해주기
  for x, y, diff in diffuse:
    room[x][y] += diff

  # 공기청정기 돌리기
  for i in range(2):
    x, y = machine[i]
    y += 1
    tmp = room[x][y]
    room[x][y] = 0
    for v in range(4):
      nx, ny = x, y
      while True:
        # 위칸 청정기의 경우 반시계방향
        if not i:
          nx = nx + dx[v]
          ny = ny + dy[v]
        # 아래칸은 시계방향
        else:
          nx = nx + dx[-v]
          ny = ny + dy[-v]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
          break
        if room[nx][ny] == -1:
          break
        tmp, room[nx][ny] = room[nx][ny], tmp
        x, y = nx, ny

# 공기청정기는 -1, 2칸이므로 2를 더해줌
print(sum([sum(x) for x in room]) + 2)
```
- 시간복잡도 : O(T x RC)
- 공간복잡도 : O(RC + R)
- 문제 유형 : 구현, 시뮬레이션
- Pypy3 제출, 230420KB / 1220ms