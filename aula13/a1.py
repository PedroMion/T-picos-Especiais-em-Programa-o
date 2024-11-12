import sys
input = sys.stdin.read

def solve(arr, n):
    arr.sort(reverse=True)

    for i in range(n, 0, -1):
        found = False
        for j in range(len(arr)):
            y = arr[j]
            while y > 0 and y != i:
                y //= 2
            if y == i:
                arr[j] = 0
                found = True
                break
        if not found:
            return False
    return True

def main():
    input = sys.stdin.read
    data = input().split("\n")
    t = int(data[0])
    index = 1

    for _ in range(t):
        arr = []
        n = int(data[index])
        index += 1

        while len(arr) < n:
            line = data[index].split(" ")
            for elem in line:
                if line != '':
                    arr.append(int(elem))
            index += 1

        if solve(arr, n):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
