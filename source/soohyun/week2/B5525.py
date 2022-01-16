# 백준 5525 IOIOI
# https://www.acmicpc.net/problem/5525

N = int(input())
M = int(input())
S = input()
count = 0 # 반복 횟수
answer = 0
i = 1

while i < M-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I': # P의 패턴과 같다면
        count += 1 # 반복 횟수에 +1
        if count == N: # 반복횟수와 N이 같은 경우 P가 포함되어 있는 것이므로 answer에 +1
            count -= 1 # P가 다음에 또 반복될 수 있으므로 count에 -1을 한다 (초기화 X)
            answer += 1
        i += 1 # 다음 문자에서는 어차피 패턴이 'OIO'가 되므로 볼 필요가 없으니까 i에 +1
    else: # P의 패턴과 다르다면 count 초기화
        count = 0
    i += 1
print(answer)