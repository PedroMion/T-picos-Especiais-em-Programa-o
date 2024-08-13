# 0 1 2 3
# 0 0 0 
# 1 -> 1 1 1 1 1 1 1 1
# 2 -> 1 2 4 3 1 2 4 3
# 3 -> 1 3 4 2 1 3 4 2
# 4 -> 1 4 1 4 1 4 1 4

def calcula_para_n(n):
    v = n % 4

    if v == 0:
        return 4
    else:
        return 0

def forca_bruta(n):
    return (1 + 2**n + 3**n + 4**n) % 5

for i in range(1000):
    test = calcula_para_n(i)
    real = forca_bruta(i)

    if(test != real):
        print(f'Errado para n = {i}')
