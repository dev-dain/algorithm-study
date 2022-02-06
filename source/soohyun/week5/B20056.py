# 백준 20056 마법사 상어와 파이어볼
# https://www.acmicpc.net/problem/20056

from collections import deque

N, M, K = map(int, input().split())
fireballs = deque()
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

for _ in range(K):
    graph = [[deque() for _ in range(N)] for _ in range(N)]

    # 파이어볼 이동하기
    while fireballs:
        r, c, m, s, d = fireballs.popleft()
        nr = (r + s * dx[d]) % N # 1-N번 행 연결
        nc = (c + s * dy[d]) % N # 1-N번 열 연결
        graph[nr][nc].append([m, s, d])

    for r in range(N):
        for c in range(N):
            if len(graph[r][c]) > 1: # 같은 칸에 파이어볼이 여러 개인 경우
                sum_m, sum_s, even, odd, cnt = 0, 0, 0, 0, len(graph[r][c]) # 질량합, 속력합, 짝수개수, 홀수개수, 파이어볼 개수
                while graph[r][c]:
                    m, s, d = graph[r][c].popleft()
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0: even += 1
                    else: odd += 1
                
                if even == cnt or odd == cnt: nd = [0, 2, 4, 6] # 방향이 모두 홀수거나 짝수인 경우
                else: nd = [1, 3, 5, 7]

                if sum_m // 5 > 0: # 질량이 0이상 이라면 파이어볼 큐에 추가 (질량이 0이면 소멸)
                    for d in nd:
                        fireballs.append([r, c, sum_m // 5, sum_s // cnt, d])
            elif len(graph[r][c]) == 1: # 같은 칸에 파이어볼이 1개인 경우 -> 파이어볼 큐에 추가
                fireballs.append([r, c] + graph[r][c].popleft())

print(sum([f[2] for f in fireballs])) # 남아있는 파이어볼의 질량 합