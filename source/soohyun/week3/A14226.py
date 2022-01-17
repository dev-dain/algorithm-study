# 백준 14226 이모티콘
# https://www.acmicpc.net/problem/14226

from collections import deque

n = int(input())
emogi = [[-1] * (n+1) for _ in range(n+1)]

def bfs():
    queue = deque([[1, 0]])
    emogi[1][0] = 0

    while queue:
        # 화면에 이모티콘 개수, 클립보드 이모티콘 개수
        s, c = queue.popleft()
        # 화면에 있는 이모티콘을 모두 클립보드에 저장
        if emogi[s][s] == -1:
            queue.append([s, s])
            emogi[s][s] = emogi[s][c] + 1
        # 클립보드에 있는 이모티콘을 모두 화면에 붙여넣기
        if s + c <= n and emogi[s+c][c] == -1:
            queue.append([s+c, c])
            emogi[s+c][c] = emogi[s][c] + 1
        # 화면에 있는 이모티콘 중 하나 삭제
        if s - 1 >= 0 and emogi[s-1][c] == -1:
            queue.append([s-1, c])
            emogi[s-1][c] = emogi[s][c] + 1

bfs()
answer = min([x for x in emogi[n] if x != -1])
print(answer)