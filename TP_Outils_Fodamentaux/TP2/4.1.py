def listePremiers(n):
    lst = []
    premier = True
    if n < 2:
        return "NAH"

    for x in range(2, n + 1):
        for i in range(2, x):
            if x % i == 0:
                premier = False
            else:
                pass

        if premier == True:
            lst.append(x)
        else:
            premier = True

    return lst

print(listePremiers(100000))