def parsing(s):
    parts = [p.strip() for p in s.split(',') if p.strip()]
    ranges = []
    for p in parts:
        a, b = p.split('-')
        ranges.append((int(a), int(b)))
    return ranges

def gift_shop2(ranges):
    invalid = set()
    maxr = max(r for (_, r) in ranges)
    max_digits = len(str(maxr))
    for k in range(1, max_digits + 1):
        max_r = max_digits // k
        if max_r < 2:  
            continue
        tenpowk = 10 ** k
        for r in range(2, max_r + 1):
            numerator = 10 ** (k * r) - 1
            denominator = tenpowk - 1
            multiplier = numerator // denominator

            a_min = 1 if k == 1 else 10 ** (k - 1)
            a_max = 10 ** k - 1

            for (L, R) in ranges:
                a_low = (L + multiplier - 1) // multiplier  
                a_high = R // multiplier                    

                if a_low < a_min:
                    a_low = a_min
                if a_high > a_max:
                    a_high = a_max

                if a_low <= a_high:
                    for a in range(a_low, a_high + 1):
                        n = a * multiplier
                        if L <= n <= R:
                            invalid.add(n)
    return sum(invalid)

with open('inputfilen2.txt') as f:
    s = f.read().strip()
ranges = parsing(s)
print("Answer:", gift_shop2(ranges))