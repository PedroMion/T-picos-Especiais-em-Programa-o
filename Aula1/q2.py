def verifyVladCandies(types, candies):
    if types <= 1:
        if candies[0] == 1:
            print("YES")
            return
        print("NO")
        return
    
    candies.sort()
    if candies[-1] - candies[-2] > 1:
        print("NO")
        return
    print("YES")

qntInputs = int(input(""))

for i in range(qntInputs):
    types = int(input(""))
    candies = input("")
    arrCandies = [int(elem) for elem in candies.split(" ")]
    verifyVladCandies(types, arrCandies)