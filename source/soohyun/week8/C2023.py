# 백준 2023 신기한 소수
# https://www.acmicpc.net/problem/2023

n = int(input())
start = [2, 3, 5, 7] # 한자리 소수

# 소수 판별
def isPrime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

# 신기한 소수 구하기
def solve(num):
    # n자리의 신기한 소수라면 출력
    if len(str(num)) == n:
        print(num)
        return

    # 기존 숫자에 0~9까지 숫자를 더해서 소수이면 다음 소수를 구한다
    for i in range(10):
        temp = num * 10 + i
        if isPrime(temp):
            solve(temp)
        
for s in start:
    solve(s)