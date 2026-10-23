def DivEuclidenne(x, y):
    quotient = x // y
    reste = x % y
    print(quotient, reste)
    print(quotient * y + reste == x)

DivEuclidenne(2026, 7)