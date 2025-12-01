import math
def countzerob(inputarr):
    current = 50
    count = 0

    for arr in inputarr:
        direction = 1 if arr[0] == "R" else -1
        distance = int(arr[1:])

        if direction == 1:
            count += (current + distance) // 100
        else:
            count += math.ceil(current / 100) - math.ceil((current - distance) / 100)
        
        current = (((current + direction * distance) % 100) + 100) % 100
    return count

with open('inputfilen1.txt', 'r') as f:
    inputarr = [line.strip() for line in f.readlines()]

print(f"{countzerob(inputarr)}")
