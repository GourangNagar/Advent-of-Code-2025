def maxjolt(line: str) -> int:
    s = line.strip()
    n = len(s)
    if n < 2:
        return 0

    maxsuffix = [-1] * n
    maxd = -1
    for i in range(n - 1, -1, -1):
        maxsuffix[i] = maxd
        d = ord(s[i]) - 48 
        if d > maxd:
            maxd = d

    best = 0
    for i in range(n - 1):
        right_max = maxsuffix[i]
        if right_max >= 0:
            tens = ord(s[i]) - 48
            cand = 10 * tens + right_max
            if cand > best:
                best = cand
    return best

def day_three(path: str) -> int:
    total = 0
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += maxjolt(line)
    return total

print("Answer:", day_three('inputfilen3.txt'))