map = {
    '(': ')',
    '[': ']'
}

def verify(str):
    stack = []

    for char in str:
        if char in map:
            stack.append(char)
        else:
            if len(stack) == 0:
                print('No')
                return
            elif map[stack[-1]] == char:
                stack.pop()
            else:
                print('No')
                return

    print('Yes') if len(stack) == 0 else print('No') 
    

qnt = int(input(""))

for i in range(qnt):
    str = input("")
    verify(str)