stone, jump = map(int, input().split())

stones = [0]
inp = input().split(" ")

for elem in inp:
    stones.append(int(elem))

for i in range(1, stone):
    stones[i] += stones[i - 1]

resp = float('inf')
for i in range(stone - jump):
    resp = min(resp, stones[i + jump] - stones[i])

print(int(resp))