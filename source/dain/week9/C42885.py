from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    boat = 0
    while people:
        boat += 1
        weight = 0
        weight += people.pop()
        if people:
            if people[-1] + weight <= limit:
                people.pop()
                continue
            if people[0] + weight <= limit:
                people.popleft()
    return boat