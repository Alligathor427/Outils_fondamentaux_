import time

def duree(fonction, argument):
    """Renvoie le temps d'exécution de fonction(argument), en secondes."""
    debut = time.perf_counter()
    fonction(argument)
    return time.perf_counter() - debut

def fibonacci(n):
    precedent, courant = 0, 1
    for _ in range(n):
        precedent, courant = courant, precedent + courant
    return precedent

def fibonacci_recursif(n):
    if n < 2:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

print(all(fibonacci(n) == fibonacci_recursif(n) for n in range(26)))
print(f"F(30) en {duree(fibonacci, 30):.6f} s")
grand = fibonacci(10_000)
print(len(str(grand)), "chiffres")