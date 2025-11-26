import math
from itertools import count

def rational_numbers():
    yield (0, 1)

    for s in count(1):
        for q in range(1, s + 1):
            p_abs = s - q
            if p_abs == 0:
                continue
            if math.gcd(p_abs, q) != 1:
                continue
            yield (-p_abs, q)
            yield (p_abs, q)

n = 100000000

gen = rational_numbers()
for _ in range(n):
    p, q = next(gen)
    print(f"{p}/{q} = {p/q}")