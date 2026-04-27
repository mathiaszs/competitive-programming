V = int(input())
P = int(input())

if V % P == 0:
    for _ in range(P):
        print(int(V / P))
else:
    sobra = V % P

    for _ in range(sobra):
        print(V // P + 1)
    for _ in range(P - sobra):
        print(V // P)

s = 0
