import math

def racines_naif(a, b, c):
    dlt = b * b - 4 * a * c
    if dlt < 0:
        raise ValueError("pas de valeurs")
    return (-b - math.sqrt(dlt)) / (2 * a), (-b + math.sqrt(dlt)) / (2 * a)

val1, val2 = racines_naif(1, -1e8, 1)
print(val1, val2)
print(val1 * val2)
