import math

def main():
    tc = int(input())
    
    for _ in range(tc):
        a, b = map(int, input().split())
        input()
        
        total_distance = 0.0

        while True:
            try:
                x1, y1, x2, y2 = map(int, input().split())
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / 1000
                total_distance += distance
            except ValueError:
                break
        
        total_distance *= 2
        total_distance /= 20

        hours = int(total_distance)
        minutes = (total_distance - hours) * 60
        minutes = round(minutes)

        if minutes == 60:
            hours += 1
            minutes = 0

        print(f"{hours}:{minutes:02d}")
        if _ < tc - 1:
            print()

if __name__ == "__main__":
    main()
