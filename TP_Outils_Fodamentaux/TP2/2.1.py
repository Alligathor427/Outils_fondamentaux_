def pgcd_naif(a, b):
    val = 1
    for i in range(1, min(a, b)):
        if a % i == 0 | b % i == 0:
            val = i
    return val

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(pgcd_naif(1071, 462), pgcd(1071, 462))