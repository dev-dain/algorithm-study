# 백준 1062 가르침
# https://www.acmicpc.net/problem/1062

n, k = map(int, input().split())
words = [input() for _ in range(n)]
learn = [0] * 26 # 읽을 수 있는 알파벳
ans = 0 # 읽을 수 있는 단어 최대 개수

# 공통 알파벳은 읽기 처리
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

def dfs(cnt, idx):
    global ans

    # 읽을 수 있는 글자가 k개인 경우 읽을 수 있는 단어 개수 세기
    if cnt == k-5:
        read = 0
        for word in words:
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    break
            else:
                read += 1
        ans = max(ans, read)

    # 글자 배우기
    for i in range(idx+1, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(cnt+1, i)
            learn[i] = 0

if k < 5:
    print(0)
else:
    dfs(0, 0)
    print(ans)