import math


n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))
dic = {}

def sleepHours(day, hour, resp, index):
    if index == n:
        return resp + 1 if r >= hour >= l else resp

    if index in dic and (day, hour) in dic[index]:
        return dic[index][(day, hour)]

    if r >= hour >= l:
        resp += 1

    awake = a[index]

    next_day = day + 1 + math.floor((awake + hour) / h)
    next_hour = (awake + hour) % h

    result = max(
        sleepHours(next_day, next_hour, resp, index + 1),
        sleepHours(next_day, (next_hour - 1 if next_hour > 0 else h-1), resp, index + 1)
    )

    if index not in dic:
        dic[index] = {}
    dic[index][(day, hour)] = result

    return result

print(max(sleepHours(0, a[0]-1, 0, 1), sleepHours(0, a[0], 0, 1)))
