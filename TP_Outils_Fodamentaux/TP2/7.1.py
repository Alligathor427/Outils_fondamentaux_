def euclide(a, b):
    if b  == 0:
        return a, 1, 0
    g, u, v = euclide(b, a % b)
    return g, v, u - (a // b) * v

g, u, v = euclide(1071, 462)
print(g, u, v)
print(1071 * u + 462 * v == g)