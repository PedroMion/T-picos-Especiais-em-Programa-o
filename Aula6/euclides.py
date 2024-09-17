def euclides(dividendo,divisor,x1=1,x2=0,y1=0,y2=1):
    quociente,resto = divmod(dividendo, divisor)
    return (divisor, x2,y2) if not resto else euclides(divisor, resto,x2,(x1-x2*quociente), y2,(y1-y2*quociente )) 

try:
    while True:
        inp = input()
        arr = inp.split(" ")

        val1 = abs(int(arr[0]))
        val2 = abs(int(arr[1]))

        if val1 == 0 and val2 == 0:
            print("1 0 0")
        elif val1 == 0:
            print(f'0 1 {val2}')
        elif val2 == 0:
            print(f'1 0 {val1}')
        else:
            a, b, c = euclides(val1, val2)
            print(f'{b} {c} {a}')

except:
    pass
