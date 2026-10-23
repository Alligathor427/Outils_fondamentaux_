import math
def racine(a, tolerance=1e-12):
    if a < 0:
        raise ValueError("cette valeur n'existe pas")
    if a == 0:
        return 0.0
    x = float(a)
    tours = 0
    while True:
        suivant = 0.5 * (x + a / x)
        tours = tours + 1
        if abs(suivant - x) <= tolerance * abs(suivant):
            return suivant
        x = suivant

print(racine(2))
print(math.sqrt(2))
print(abs(racine(2) - math.sqrt(2)) < 1e-12)

