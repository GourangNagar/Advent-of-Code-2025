def maxk(line: str, k: int = 12) -> str:
    s = line.strip()
    n = len(s)
    if k <= 0:
        return ""
    if k >= n:
        return s 

    res = []
    start = 0
    for pos in range(k):
        last_inclusive = n - (k - pos)
        best_digit = '-1'
        best_idx = start
        for i in range(start, last_inclusive + 1):
            if s[i] > best_digit:
                best_digit = s[i]
                best_idx = i
                if best_digit == '9':
                    break
        res.append(best_digit)
        start = best_idx + 1
    return ''.join(res)


def day_three(path: str, k: int = 12) -> int:
    total = 0
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            chosen = maxk(line, k)
            total += int(chosen)
    return total

print("Answer:", day_three('inputfilen3.txt', 12))