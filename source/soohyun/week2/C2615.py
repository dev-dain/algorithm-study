# 백준 2615 오목
# https://www.acmicpc.net/problem/2615

graph = [list(map(int, input().split())) for _ in range(19)]
dx, dy = [-1, 0, 1, 1], [1, 1, 1, 0] # 북동, 동, 남동, 남
color, ax, ay = 0, -1, -1 # 이긴 바둑알, 가장 왼쪽 바둑돌의 위치

def omok(x, y):
    for i in range(4):
        # 반대방향에 있는 바둑알이 바둑판 범위를 벗어나거나 현재 바둑돌과 다르다면 6목이 아니다
        bx = x - dx[i]
        by = y - dy[i]
        if (bx < 0 or bx >= 19 or by < 0 or by >= 19) or graph[bx][by] != graph[x][y]: # 6목이 아닌 경우
            # 다음 바둑알 위치
            nx = x + dx[i]
            ny = y + dy[i]
            cnt = 1 # 연속된 바둑알 개수

            # 다음 바둑알이 바둑판 범위에 있고 현재 바둑돌과 같을 때까지 연속된 바둑알 개수를 센다
            while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == graph[x][y]:
                cnt += 1
                nx += dx[i]
                ny += dy[i]

            # 연속된 바둑알이 5개라면 true 리턴
            if cnt == 5:
                return True
                    
    return False # 승부가 결정나지 않는 경우 false 리턴
        

for i in range(19):
    for j in range(19):
        if graph[i][j] != 0: # 알이 있는 위치면 탐색 수행
            if omok(i, j): # 승부가 결정나면 결과값 저장 후 탐색 종료
                color, ax, ay = graph[i][j], i+1, j+1
                break

print(color)
if color != 0:
    print(ax, ay)