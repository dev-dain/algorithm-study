# 프로그래머스 49191 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

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