from collections import defaultdict
# 접시 n, 초밥 d, 연속먹기 k, 쿠폰 번호 c
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

case = set()
case_cnt = defaultdict(int)
answer = 0

left = 0
right = k-1

for i in range(k):
    case.add(sushi[i])
    case_cnt[sushi[i]] += 1

for i in range(n):
    case_cnt[sushi[left]] -= 1
    if case_cnt[sushi[left]] == 0:
        case.remove(sushi[left])
    left = (left+1) % n

    right = (right+1) % n
    if sushi[right] not in case:
        case.add(sushi[right])
    case_cnt[sushi[right]] += 1

    if c not in case:
        total_case = len(case)+1
    else:
        total_case = len(case)
    
    answer = max(answer, total_case)
print(answer)