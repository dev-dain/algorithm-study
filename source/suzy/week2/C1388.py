# 세로 n 가로 m
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))
  
answer = 0

# 행
for i in range(n):
    v ='/'
    for j in range(m):
        if graph[i][j] == '-':
            if graph[i][j] != v:
                answer += 1
        v = graph[i][j]

# 열
for i in range(m):
    v = '/'
    for j in range(n):
        if graph[j][i] =='|':
            if graph[j][i] != v:
                answer += 1
        v = graph[j][i]
print(answer)