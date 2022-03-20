# 백준 14890 경사로
# https://www.acmicpc.net/problem/14890

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0 # 지나갈 수 있는 길의 개수

def check(road):
    slope = [0] * n # 경사로가 놓인 위치

    for i in range(n-1):
        # 높이가 같은 경우
        if road[i] == road[i+1]:
            continue

        # 높이 차가 2 이상인 경우
        if abs(road[i] - road[i+1]) > 1:
            return False
            
        # 높이 차가 1인 경우
        # 높이가 낮아지는 경우
        if road[i] > road[i+1] and i+1+l <= n:
            for j in range(i+1, i+1+l):
                if slope[j] or road[j] != road[i+1]: # 이미 경사로를 놓았거나 경사로 높이가 다른 경우
                    return False
                slope[j] = 1
        # 높이가 높아지는 경우
        elif road[i] < road[i+1] and i-l >= -1:
            for j in range(i, i-l, -1):
                if slope[j] or road[j] != road[i]: # 이미 경사로를 놓았거나 경사로 높이가 다른 경우
                    return False
                slope[j] = 1
        # 경사로를 높을 수 있는 범위를 벗어난 경우
        else:
            return False

    return True

# 가로 길
for i in range(n):
    if check(board[i]):
        ans += 1

# 세로 길
for j in range(n):
    temp = []
    for i in range(n):
        temp.append(board[i][j])
    if check(temp):
        ans += 1

print(ans)