# 백준 15684 사다리 조작
# https://www.acmicpc.net/problem/15684

import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
board = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1 # 가로선 연결

# i번 세로선의 결과가 i번이 나오는지 확인
def check():
    for start in range(n): # 세로선(열) 체크
        j = start # 이동하는 가로선
        for i in range(h): # 가로선(행) 체크
            if board[i][j]: # 가로선이 오른쪽에 있다면 오른쪽으로 이동
                j += 1
            elif j > 0 and board[i][j-1]: # 가로선이 왼쪽에 있다면 왼쪽으로 이동
                j -= 1
        if j != start: # 도착한 세로선이 출발한 세로선과 같지 않으면 return False
            return False
    return True # i번 세로선의 결과가 i번이 나오면 return True

# 가로선 놓기
def solve(cnt, x, y):
    global ans

    # 모든 i번 세로선의 결과가 i번이 나온다면 답을 구하고 리턴
    if check():
        ans = min(ans, cnt)
        return
    # 더 이상 가로선을 놓을 수 없거나 (최대 가로선 수는 3) 가로선이 답보다 많다면 더 이상 볼 필요가 없으므로 리턴
    elif cnt == 3 or ans <= cnt:
        return

    for i in range(x, h):
        k = y if i == x else 0 # 행이 변경되면 0부터, 변경되지 않으면 현재 가로선을 탐색
        for j in range(k, n-1):
            # 현재 가로선이 없으며 왼쪽과 오른쪽에 가로선이 없는 경우 가로선을 놓는다
            if not board[i][j] and not board[i][j+1] and not board[i][j-1]:
                board[i][j] = 1
                solve(cnt+1, i, j+2)
                board[i][j] = 0

ans = 4
solve(0, 0, 0)
print(ans) if ans < 4 else print(-1)