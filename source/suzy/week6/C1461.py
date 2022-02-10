# 책 수 N 한 번에 들 수 있는 책 수 M
N, M = map(int, input().split())

arr = list(map(int, input().split()))

left = []
right = []
max_value = 0
for i in arr:
    if i < 0:
        left.append(i)
    else:
        right.append(i)
    if abs(i) > abs(max_value):
        max_value = i

dist = []
right.sort(reverse=True)
left.sort()

for i in range(0, len(right), M):
    if right[i] != max_value:
        dist.append(right[i])

for i in range(0, len(left), M):
    if left[i] != max_value:
        dist.append(left[i])

answer = abs(max_value)
for i in dist:
    answer += abs(i * 2)
    
print(answer)