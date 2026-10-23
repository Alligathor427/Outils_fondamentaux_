def fact(n):
    resultat = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat.append(d)
            n = n // d
        d = d + 1
    if n > 1:
        resultat.append(n)
    return resultat

def produit(p, n):
    produit = p
    for x in n:
        produit = produit * x
    return produit

print(fact(360))
print(produit(1, fact(360)))