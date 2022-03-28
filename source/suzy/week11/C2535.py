n = int(input())
oly = []
for _ in range(n):
    # 참가국 학생번호 성적
    oly.append(list(map(int, input().split(' '))))

oly.sort(key=lambda x: x[2], reverse=True)

# 상위 수상자 2명 차례대로 금메달 은메달
gold = oly[0]
silver = oly[1]
# 동메달 앞선 메달권 같은나라일 경우 X
bronze = None

for i in range(2, len(oly)):
    if gold[0] == silver[0] == oly[i][0]:
        continue
    else:
        bronze = oly[i]
        break

print(gold[0],gold[1])
print(silver[0],silver[1])
print(bronze[0],bronze[1])