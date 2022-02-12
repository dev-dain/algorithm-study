n, s = map(int, input().split())

arr = list(map(int, input().split()))

end = 0
# 초기의 합을 arr[0]
result = arr[0]
ans = float('inf')

# 투포인터
for start in range(n):
    while result < s and end < n:
        end += 1
        if end == n:
            break
        result += arr[end]
    
    if result >= s:
        ans = min(ans, end-start+1)
    result -= arr[start]

if ans == float('inf'):
    print(0)
else:
    print(ans)