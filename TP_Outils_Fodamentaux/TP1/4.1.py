def nombre_de_chiffres(n):
    compteur = 1
    while n >= 10:
        n = n // 10
        compteur += 1
    print(compteur)

nombre_de_chiffres(2566)


