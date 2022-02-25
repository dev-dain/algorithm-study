# 백준 17136 색종이 붙이기
# https://www.acmicpc.net/problem/17136

paper = [list(map(int, input().split())) for _ in range(10)]
paper_cnt = [0] * 6 # 종이별 사용 개수
ans = 1e9 # 색종이의 최소 개수

def solve(x, y, cnt):
    global ans

    if y >= 10: # 끝까지 탐색한 것이므로 최소 개수 갱신
        ans = min(ans, cnt)
        return

    if x >= 10: # y열은 탐색이 끝났으므로 다음 열로 넘어간다
        solve(0, y+1, cnt)
        return

    if paper[x][y] == 1: # 색종이를 붙일 수 있는 경우
        for k in range(1, 6): # k = 색종이의 크기
            if paper_cnt[k] == 5: # 해당 색종이 사용 개수가 5인 경우 다음 색종이로 넘어간다
                continue

            if x+k > 10 or y+k > 10: # 범위를 벗어나는 크기의 색종이라면 break
                break

            flag = True # 해당 색종이를 붙일 수 있는지 체크
            for i in range(x, x+k):
                for j in range(y, y+k):
                    if paper[i][j] == 0: # 해당 색종이를 붙일 수 없다먄 flag = False
                        flag = False
                        break
                if not flag: break

            if flag: # 해당 색종이를 붙일 수 있는 경우
                # 색종이를 붙이는 칸을 0으로 만들고 개수에 +1
                for i in range(x, x+k):
                    for j in range(y, y+k):
                        paper[i][j] = 0
                paper_cnt[k] += 1

                solve(x+k, y, cnt+1) # 다음 칸으로 넘어간다

                # 초기화
                for i in range(x, x+k):
                    for j in range(y, y+k):
                        paper[i][j] = 1
                paper_cnt[k] -= 1
    else: # 색종이를 붙일 수 없는 경우
        solve(x+1, y, cnt) # 다음 칸으로 넘어간다

solve(0, 0, 0)
print(-1) if ans == 1e9 else print(ans)