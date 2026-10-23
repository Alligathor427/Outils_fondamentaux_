import fractions

total = Fraction(0)
for _ in range(1000):
    total = total + Fraction(1, 10)
print(total, total == 100)
print(Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10))