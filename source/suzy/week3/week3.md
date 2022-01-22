## 3주차
### 1) [백준 1504] (https://www.acmicpc.net/problem/1504)
- 문제 유형: 그래프, 다익스트라
- 시간 복잡도: O(ElogV)  |  공간 복잡도: O(n)
- 접근 방법
    - " 방향성이 없는 그래프 " , " 최단 경로로 이동 " -> 방향이 없는 그래프, 다익스트라 문제
    - 두 정점 v1, v2 를 반드시 경유해야한다
<br/><br/>
* 풀이
  * 1 (2 -> 3) 4 과 1 (3 -> 2) 4 두 경로를 비교하여 더 작은 값을 출력한다
  * 경로가 없을 경우 -1 를 출력한다
<br/><br/>
- 코드
```python
import heapq
import sys
input = sys.stdin.readline

INF = float('inf')

# 노드 N 간선 E
N, E = map(int, input().split())
road = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    road[a].append([c,b])
    road[b].append([c,a])

# 반드시 거쳐야하는 두 정점
v1, v2 = map(int, input().split())

def dijkstra(start, end):
    dist = [INF] * (N+1)
    dist[start] = 0

    heap = []
    heapq.heappush(heap, [0, start])
  
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for c, n in road[node]:
            if dist[n] > dist[node] + c:
                dist[n] = dist[node] + c
                heapq.heappush(heap, [dist[n], n])
    return dist[end]

# 1 (2-3) 4
path1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,N)
# 1 (3-2) 4
path2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,N)

result = min(path1, path2)
print(result if result < INF else -1)
```
---

### 2) [백준 1987] (https://www.acmicpc.net/problem/1987)
- 문제 유형: 그래프, BFS 백트래킹 
- 시간 복잡도: O(N+E) |  공간 복잡도: O(n)
- 접근 방법
    - 같은 알파벳일 경우 이동할 수 없다 ...
    - 상하좌우로 움직이며 최대 몇 칸을 이동할 수 있는지 구한다
<br/><br/>
* 풀이
  * 방향벡터를 사용하여 상하좌우로 움직이며 순회한다
  * BFS 로 한칸씩 확인하지만 조건을 만족하지 않을 경우 백트래킹 ! ( deque -> set 사용 )
<br/><br/>
- 코드
```python
# 세로 R 가로 C
R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(input().strip())

# 방향벡터
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    # 1행 1열일 경우
    ans = 1
    q = set([(x, y, graph[x][y])])
    
    while q:
        x, y, g = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않고 알파벳이 같지 않을 경우 !
            if 0<=nx<R and 0<=ny<C and graph[nx][ny] not in g:
                q.add((nx, ny, g + graph[nx][ny]))
                ans = max(ans, len(g)+1)
    return ans

print(bfs(0,0))
```
---

### 3) [프로그래머스 49191] (https://programmers.co.kr/learn/courses/30/lessons/49191)
- 문제 유형: 그래프, 플로이드워셜
- 시간 복잡도:  O(N^3)  |  공간 복잡도: O(n)
- 접근 방법
    - 순위를 정하기 위해서 n-1 명과 싸운다
    - 다른 사람의 승패를 통해 순위가 정해진다 (플로이드워셜)
<br/><br/>
* 풀이
  * 문제 이해가 잘 안되서 인터넷에 여러 풀이를 찾아봤습니다
  *  i 한테 진 애들은 i 를 이긴 애들한테도 진다 / i 를 이긴 애들은 i 한테 진 애들도 이긴다
  * 중복을 없애기 위해 set 을 사용합니다
<br/><br/>
- 코드
```python
from collections import defaultdict
def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    
    for i,j in results:
        win[j].add(i) # 이긴사람 : 이긴사람한테 진사람
        lose[i].add(j) # 진사람 : 진사람을 이긴사람
    
    print(win)
    # 1번부터 N번까지 선수
    for i in range(1, n+1):
        # i한테 진 애들은 i를 이긴 애들한테도 짐
        for w in win[i]:
            lose[w].update(lose[i])
        # i를 이긴 애들은 i한테 진 애들한테도 이김
        for l in lose[i]:
            win[l].update(win[i])
        
    # i한테 이기고 진애들을 합쳐서 n-1 이면 순위가 정해진것
    for i in range(1,n+1):
        if len(win[i])+len(lose[i]) == n-1:
            answer += 1
    
    return answer
```

