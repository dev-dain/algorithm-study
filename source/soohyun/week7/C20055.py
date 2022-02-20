# 백준 20055 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055

from collections import deque

n, k = map(int, input().split())
a = deque(map(int, input().split()))
robot = deque([0] * n)
ans = 1 # 몇 번째 단계

while True:
    # 1. 벨트와 로봇이 1칸 회전한다
    a.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0 # 내리는 위치

    # 2. 벨트가 회전하는 방향으로 로봇이 1칸 이동할 수 있다면 이동한다
    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and a[i+1] >= 1: # 이동하려는 칸에 로봇이 없으며 내구성이 1이상 이라면
            a[i+1] -= 1
            robot[i], robot[i+1] = 0, robot[i]
    robot[n-1] = 0 # 내리는 위치

    # 3. 올리는 위치에 로봇을 올린다
    if robot[0] == 0 and a[0] > 0: # 내구도가 0이 아니라면
        a[0] -= 1
        robot[0] = 1

    # 4. 내구도가 0인 칸의 개수가 k개 이상이라면 종료한다
    if a.count(0) >= k:
        break

    ans += 1

print(ans)