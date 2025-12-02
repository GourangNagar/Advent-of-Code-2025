def parsing(s):
    parts = [p.strip() for p in s.split(',') if p.strip()]
    ranges = []
    for p in parts:
        a, b = p.split('-')
        ranges.append((int(a), int(b)))
    return ranges

def gift_shop(ranges):
    total = 0
    maxr = max(r for (_, r) in ranges)
    for k in range(1, (len(str(maxr))  // 2) + 1):
        multiplier = 10**k + 1  
        a_min_by_digits = 1 if k == 1 else 10**(k-1)
        a_max_by_digits = 10**k - 1

        for (L, R) in ranges:
            a_low = (L + multiplier - 1) // multiplier  
            a_high = R // multiplier                   
            a_low = max(a_low, a_min_by_digits)
            a_high = min(a_high, a_max_by_digits)
            if a_low <= a_high:
                for a in range(a_low, a_high + 1):
                    n = a * multiplier
                    if L <= n <= R:
                        total += n
    return total

with open('inputfilen2.txt') as f:
    inputstr = f.read().strip()
ranges = parsing(inputstr)
print("Answer:", gift_shop(ranges))