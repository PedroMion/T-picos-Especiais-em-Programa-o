def fractions(k):
    result = []
    for y in range(k+1, (2*k) + 1):
        if (k * y) % (y - k) == 0:
            x = (k*y) // (y - k)
            result.append(f'1/{x} + 1/{y}')
    
    print(len(result))
    for val in result:
        print(f'1/{k} = {val}')

try:
    while True:
        inp = int(input())
        fractions(inp)
except:
    pass
