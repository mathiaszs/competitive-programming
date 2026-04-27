import math

A, B, C, D = map(int, input().split())

if B != D:
    A = A * D
    C = C * B

    den = B * D
else:
    den = B

num = A + C

g = math.gcd(num, den)
num //= g
den //= g

print(num, den)
