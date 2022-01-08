def solution(numbers, target):
    answer = 0
    check = [0]

    for num in numbers:
        tmp = []
        for number in check:
            tmp.append(number + num)
            tmp.append(number - num)
        check = tmp

    for i in check:
        if i == target:
            answer += 1

    return answer