N = int(input())
D = int(input())
A = int(input())

if A < D:
    print(D - A)
elif A == D:
    print(0)
else:
    resultado = N - A + D
    print(resultado)
