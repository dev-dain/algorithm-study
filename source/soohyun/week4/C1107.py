# 백준 1107 리모컨
# https://www.acmicpc.net/problem/1107

N = int(input())
M = int(input())
button = []
if M:
    button = list(map(int, input().split()))
count = abs(N - 100)

for num in range(1000001): # 큰 수에서 작은 수로 내려오는 경우를 생각하여 1000000까지 탐색
    for n in str(num): # 해당 채널에 고장난 버튼이 있다면 다음 채널로 넘어간다
        if int(n) in button:
            break
    else: # 해당 채널에 고장난 버튼이 없다면 횟수를 구한다
        count = min(count, len(str(num)) + abs(num - N)) # min(기존 횟수, 해당 채널을 누른 횟수 + 해당 채널과 이동하려는 채널의 차이)

print(count)