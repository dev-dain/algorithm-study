import sys, heapq
from collections import defaultdict

def solution(N, road, K):
  cost = [sys.maxsize for _ in range(N+1)]
  graph = defaultdict(list)
  for info in road:
    print(info)
    graph[info[0]].append((info[2], info[1]))
    graph[info[1]].append((info[2], info[0]))

  qu = []
  heapq.heappush(qu, (0, 1))
  cost[1] = 0
  
  while qu:
    cur_dist, node = heapq.heappop(qu)
    if cost[node] < cur_dist:
      continue
    for adj_dist, adj_node in graph[node]:
      distance = cur_dist + adj_dist
      if distance < cost[adj_node]:
        cost[adj_node] = distance
        heapq.heappush(qu, (distance, adj_node))

  return len(list(filter(lambda x: x <= K, cost)))

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))