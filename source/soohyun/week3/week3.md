## 3주차 공통문제
### [백준 1987 알파벳](https://www.acmicpc.net/problem/1987)
- 문제 유형: 그래프
- 시간 복잡도: O(V^2)
- 공간 복잡도: O(N)
- 접근 방법
    - BFS에서 큐에 방문한 알파벳 리스트를 넣어주는 것이 핵심인 문제였다.
    - 처음에 deque을 사용하여 풀었는데 시간초과가 났다.
    - 풀이를 찾아보니 set을 써야된다고 해서 deque(set()) 형태로 풀었더니 메모리 초과가 났다.
    - deque을 쓰지 않고 set만 사용하여 풀었더니 풀이가 통과되었다.
    - 중복을 없애기 위해 set을 쓰는 것을 알겠는데... 정확하게 이해를 못하겠다.
    - deque을 사용하는 것과 set을 사용하는 것의 차이를 모르겠다.
<br/><br/>
- 풀이
    1. 동서남북으로 이동할 수 있는 방향벡터를 생성한다.
    2. bfs로 지나갈 수 있는 최대 칸수를 구한다.
        - 큐에 시작점의 정보를 삽입한다.
        - 큐에서 노드 하나를 가져온 후, 최대 칸수를 갱신한다.
        - 동서남북 방향의 노드를 확인하여, 범위 내에 있으며 아직 방문하지 않은 알파벳이라면 큐에 삽입한다.
    3. 결과를 출력한다.
<br/><br/>
- 코드
```python
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
```

### [백준 1504 특정한 최단 경로](https://www.acmicpc.net/problem/1504)
- 문제 유형: 그래프, 다익스트라
- 시간 복잡도: O(ElogV)
- 공간 복잡도: O(N)
- 접근 방법
    - v1, v2를 무조건 거쳐가는 최단 경로는 두 가지가 있었다.
        1. start -> v1 -> v2 -> end
        2. start -> v2 -> v1 -> end
    - 따라서 최단경로를 구하기 위해서는 start에서 최단경로, v1에서 최단경로, v2에서 최단경로를 구한 후, 경로를 계산해주면 된다.
<br/><br/>
- 풀이
    1. 그래프 정보를 graph에 저장한다. 양방향이므로 양쪽으로 정보를 저장해야 한다.
    2. 다익스트라 알고리즘을 수행하여 start(1), v1, v2에서의 최단경로를 구한다.
        - 시작점은 경로를 0으로 설정하여 힙에 삽입하고, 최단경로는 0으로 만든다.
        - 힙에서 가장 거리가 짧은 노드(= 현재 노드)를 가져온다.
        - 현재 노드와 연결된 인접 노드를 확인하여 최단거리를 갱신한다.
    3. 최단경로를 구한 것을 사용하여 v1, v2를 지나는 최단 경로를 구한다.
    4. 경로가 없다면 -1, 있다면 3에서 구한 값을 출력한다.
<br/><br/>
- 코드
```python
import heapq, sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dist = [1e9] * (N+1) # 최단거리 리스트
    dist[start] = 0

    while queue:
        cur_dist, cur_node = heapq.heappop(queue) # 가장 거리가 짧은 노드
        if dist[cur_node] < cur_dist: # 최단거리가 현재 노드거리보다 작다면 넘어간다
            continue
        for next_node, next_dist in graph[cur_node]: # 현재 노드와 연결된 인접 노드 확인
            cost = cur_dist + next_dist
            if cost < dist[next_node]: # 현재 노드를 거쳐서 가는 거리가 다음 노드거리보다 작다면 최단거리 갱신
                heapq.heappush(queue, (cost, next_node))
                dist[next_node] = cost

    return dist

dist_start = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

# start -> v1 -> v2 -> end 와 start -> v2 -> v1 -> end 중 더 짧은 거리 구하기
answer = min(dist_start[v1] + dist_v1[v2] + dist_v2[N], dist_start[v2] + dist_v2[v1] + dist_v1[N])
print(-1) if answer >= 1e9 else print(answer) # 최단경로 유무에 따른 결과 출력
```

### [프로그래머스 49191 순위](https://programmers.co.kr/learn/courses/30/lessons/49191)
- 문제 유형: 플로이드 워셜
- 시간 복잡도: O(N^3)
- 공간 복잡도: O(N^2)
- 접근 방법
    - 먼저 2차원 리스트를 생성하여 이긴 경우에 1, 진 경우에 -1로 값을 저장한다.
    - 플로이드 워셜을 사용하여 순위를 매길 수 있는지 확인하면 된다.
<br/><br/>
- 풀이
    1. 경기 결과를 저장할 2차원 리스트(graph)를 생성한 뒤, 이긴 경우에 1, 진 경우에 -1로 값을 저장한다.
    2. 플로이드 워셜을 사용하여 순위를 매길 수 있는지 확인한다.
        - graph[i][k]와 graph[k][j]가 모두 1이라면 i가 j를 이길 수 있는 것이므로 graph[i][j] = 1
        - graph[i][k]와 graph[k][j]가 모두 -1이라면 i가 j에게 지는 것이므로 graph[i][j] = -1
    3. 결과를 출력한다.
        - graph[x].count(0) == 2인 경우만 뽑는 이유는 인덱스가 0인 것과 자기 자신을 뺀 것!
<br/><br/>
- 코드
```python
def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for A, B in results:
        graph[A][B] = 1 # 이긴 경우는 1
        graph[B][A] = -1 # 진 경우는 -1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] == 0:
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1
                    elif graph[i][k] == -1 and graph[k][j] == -1:
                        graph[i][j] = -1

    return len([x for x in range(1, n+1) if graph[x].count(0) == 2])
```