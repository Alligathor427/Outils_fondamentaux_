import time

def duree(fonction, argument):
    """Renvoie le temps d'exécution de fonction(argument), en secondes."""
    debut = time.perf_counter()
    fonction(argument)
    return time.perf_counter() - debut

def fibonacci_recursif(n):
    if n < 2:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

print([fibonacci_recursif(n) for n in range(15)])

for n in (20, 25, 30, 35):
    print(f"F({n}) : {duree(fibonacci_recursif, n):.4f} s") # La durée augmente de manière exponentielle