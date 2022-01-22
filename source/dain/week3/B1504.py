# 다익스트라는 힙
import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

# 오 완전 좋은 아이디어네
# 경유해야 할 노드가 있다면 거기까지 가는 노드의 최단경로를 구해서 합하면 된다
# 그래서 비용은 함수에서 각자 관리한다.

# 중요!
# 다익스트라를 할 때는 []가 아니라 () 튜플로 저장할 것
# 튜플로 바꾸기만 했는데 시간초과에서 벗어남.. 뭐냐
def dijkstra(start, end):
  qu = []
  heapq.heappush(qu, (0, start))
  dist = [INF for _ in range(n+1)]
  dist[start] = 0

  while qu:
    cur_cost, node = qu.pop()
    # if cur_cost > dist[node]:
    #   continue
    for adj_cost, adj_node in graph[node]:
      cost = cur_cost + adj_cost
      if cost < dist[adj_node]:
        dist[adj_node] = cost
        heapq.heappush(qu, (cost, adj_node))
  
  return dist[end]

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((c, b))
  graph[b].append((c, a))
v1, v2 = map(int, input().split())
# dist = [sys.maxsize for _ in range(n+1)]

p1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
p2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
res = min(p1, p2)
print(res if res < INF else -1)