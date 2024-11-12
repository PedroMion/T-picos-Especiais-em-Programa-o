def wow(s):
    count_w = 0
    o_index = []
    result = 0
    dic = {}

    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'v':
            count_w += 1
            continue
        elif s[i] == 'o':
            dic[i] = count_w
            o_index.append(i)
    
    for elem in o_index:
        result += (dic[elem] * (count_w - dic[elem]))
    
    return result

s = input()
print(wow(s))