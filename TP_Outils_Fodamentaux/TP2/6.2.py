appel = {}

def fibo_compte(n):
    appel[n] = appel.get(n, 0) + 1
    if n < 2:
        return n
    return fibo_compte(n - 1) + fibo_compte(n - 2)

resultat = fibo_compte(30)
print("F(30) =", resultat)
print("appels a F(1) :", appel[1])
print("appels en tout :", sum(appel.values()))