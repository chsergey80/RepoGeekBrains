from decimal import Decimal
D = Decimal
D("0.444").quantize(D("1.0000"))
print(D)