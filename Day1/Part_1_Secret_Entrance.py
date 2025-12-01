def countzeroa(inputstr):
        
    current = 50
    count = 0
    for arr in inputstr:
        direction = 1 if arr[0] == "R" else -1
        distance = int(arr[1:]) 
    
        if direction == 1:
            current=(current+distance)%100   
        else:
            current=(current-distance)%100
        
        if current == 0:
            count += 1
    return count

with open('inputfilen1.txt', 'r') as f:
    inputarr = [line.strip() for line in f.readlines()]

print(f"{countzeroa(inputarr)}")
