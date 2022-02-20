# 백준 1339 단어 수학
# https://www.acmicpc.net/problem/1339

from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]
alphabet = defaultdict(int)
ans = 0 # 최대 합

# 알파벳 자릿수 구하기
for word in words:
    for i in range(len(word)):
        num = 10 ** (len(word)-i-1)
        alphabet[word[i]] += num

alpha_sort = sorted(alphabet.items(), key = lambda x: -x[1]) # 자릿수가 높은 순으로 정렬

# 최대 합 구하기
num = 9
for a in alpha_sort:
    ans += a[1] * num
    num -= 1

print(ans)