# 백준 17609 회문
# https://www.acmicpc.net/problem/17609

T = int(input())

for _ in range(T):
    s = input()
    l = len(s)

    if s == s[::-1]:
        print(0)
        continue

    for i in range(l//2):
        if s[i] != s[l-i-1]:
            s1 = s[:l-i-1] + s[l-i:] # 오른쪽 문자열 삭제
            s2 = s[:i] + s[i+1:] # 왼쪽 문자열 삭제

            if s1 == s1[::-1] or s2 == s2[::-1]:
                print(1)
            else:
                print(2)
            break