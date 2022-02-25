# 백준 17406 배열 돌리기 4
# https://www.acmicpc.net/problem/17406

from itertools import permutations
import copy

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
rot = [list(map(int, input().split())) for _ in range(k)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
ans = 1e9 # 최종 최소값

# 회전하기
def rotate(pm, arr):
    result = 1e9 # 최소값

    for r, c, s in pm:
        r -= 1; c -= 1 # 인덱스가 0부터 시작
        lx, ly, rx, ry = r-s, c-s, r+s, c+s # 가장 왼쪽 위의 위치, 가장 오른쪽 아래의 위치

        # lx = rx and ly = ry( = 더 이상 회전할게 없다는 의미) 가 될 때까지 회전
        while lx < rx and ly < ry:
            x, y, before = lx, ly, arr[lx][ly] # 현재 위치, 값
            dir = 0 # 이동할 방향

            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]

                if nx < lx or nx > rx or ny < ly or ny > ry: # 이동 범위를 벗어나면 방향을 바꾼다
                    dir += 1
                    continue

                arr[nx][ny], before = before, arr[nx][ny] # 값 이동
                x, y = nx, ny # 위치 이동

                if x == lx and y == ly: # 회전이 끝나면 다음 회전으로 넘어간다
                    lx += 1; ly += 1; rx -= 1; ry -= 1
                    break

    # 최소값 구하기
    for row in arr:
        result = min(result, sum(row))

    return result

# 모든 회전 순서 순열에 따른 회전하기
for pm in permutations(rot, k):
    result = rotate(pm, copy.deepcopy(a))
    ans = min(ans, result)

print(ans)