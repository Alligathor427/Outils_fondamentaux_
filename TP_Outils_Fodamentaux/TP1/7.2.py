import math

def racines_naif(a, b, c):
    dlt = b * b - 4 * a * c
    if dlt < 0:
        raise ValueError("pas de valeurs")

    if b >= 0:
        resultat = (-b - math.sqrt(dlt)) / (2 * a)

    else:
        resultat = (-b + math.sqrt(dlt)) / (2 * a)

    resultat2 = c / (a * resultat)

    return min(resultat, resultat2), max(resultat, resultat2)

val1, val2 = racines_naif(1, -1e8, 1)
print(val1, val2)
print(val1 * val2)