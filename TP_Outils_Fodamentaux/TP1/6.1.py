def vers_binaire(n):
    init = ''
    while n > 0:
        if n % 2 == 1:
            init = '1' + init
        else:
            init = '0' + init
        n = n // 2
    return init

print(vers_binaire(254))

#  1111 1110 Octet