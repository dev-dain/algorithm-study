# 백준 2661 좋은수열
# https://www.acmicpc.net/problem/2661

n = int(input())
nums = [] # 좋은 수열

# 좋은 수열인지 확인
def check(arr, idx):
    for l in range(1, idx//2+1): # 비교할 부분 수열 길이
        for i in range(l, idx-l+1):
            if arr[i-l: i] == arr[i: i+l]: # 같은 부분 수열이 있는 경우
                return False
    return True

def solve(idx):
    # 좋은 수열이 아닌 경우
    if not check(nums, idx):
        return

    # 길이가 n인 가장 작은 좋은 수열인 경우 출력하고 멈춘다
    if idx == n:
        print(*nums, sep='')
        exit(0)

    # 숫자를 하나씩 넣어보면서 좋은 수열을 찾는다
    for i in range(1, 4):
        nums.append(i)
        solve(idx+1)
        nums.pop() # 초기화

solve(0)