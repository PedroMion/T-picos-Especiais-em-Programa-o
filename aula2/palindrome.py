mirror = {
    'A': 'A',
    'E': '3',
    'H': 'H',
    'I': 'I',
    'J': 'L',
    'L': 'J',
    'M': 'M',
    'O': 'O',
    'S': '2',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': '5',
    '1': '1',
    '2': 'S',
    '3': 'E',
    '5': 'Z',
    '8': '8'
}

def verifyWord(str):
    left = 0
    right = len(str) - 1
    isPalindrome = True
    isMirror = True

    while(left <= right):
        if str[left] != str[right]:
            isPalindrome = False
        if str[left] not in mirror:
            isMirror = False
        elif mirror[str[left]] != str[right]:
            isMirror = False
        left += 1
        right -= 1
    
    if isMirror and isPalindrome:
        print(f'{str} -- is a mirrored palindrome.')

    elif isMirror and isPalindrome == False:
        print(f'{str} -- is a mirrored string.')

    elif isMirror == False and isPalindrome:
        print(f'{str} -- is a regular palindrome.')
    
    else:
        print(f'{str} -- is not a palindrome.')

    print("")

while True:
    try:
        inp = input()
        verifyWord(inp)
    except EOFError:
        break