N,M,K = map(int, input().split())
# r,c,m,s,d
fire = []
for _ in range(M):
    _r,_c,_m,_s,_d = list(map(int, input().split()))
    fire.append([_r-1,_c-1,_m,_s,_d])

graph = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

# 파이어볼 이동
for _ in range(K):
    while fire:
        cr,cc,cm,cs,cd = fire.pop()
        # 1번과 N 행이 연결되어 있기 때문
        nr = (cr + cs * dx[cd]) % N
        nc = (cc + cs * dy[cd]) % N
        graph[nr][nc].append([cm,cs,cd])
        
    # 2개 이상인지 확인
    for r in range(N):
        for c in range(N):
            # 2개 이상인 경우 > 4 로 쪼개기
            if len(graph[r][c]) > 1:
                summ,sums,cnt_odd, cnt_even, cnt = 0,0,0,0,len(graph[r][c])
                while graph[r][c]:
                    _m,_s,_d = graph[r][c].pop()
                    summ += _m
                    sums += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                # 모두 홀수이거나 짝수인 경우
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]
                # 질량이 0이면 소멸
                if summ // 5:
                    for d in nd:
                        fire.append([r,c,summ//5,sums//cnt, d])
                        
            # 1개인 경우
            if len(graph[r][c]) == 1:
                fire.append([r,c]+ graph[r][c].pop())
                
print(sum([i[2] for i in fire]))