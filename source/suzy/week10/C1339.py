import sys
input = sys.stdin.readline

n = int(input())

alphabet = []
for i in range(n):
    alphabet.append(input().rstrip())

point = [0] * 26

for alpha in alphabet:
    for i, al in enumerate(alpha):
        j = len(alpha) - i -1
        point[ord(al)-ord('A')] += 10**j

point.sort(reverse = True)

sum = 0
for i in range(9, -1, -1): # 9 - 0 큰수부터 곱해준다
    sum += point[i]*(9-i)
print(sum)