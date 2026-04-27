import sys

entrada = list(map(int, input().split()))
N = entrada[0]
C = entrada[1]
Quantity = 0

for i in range(N):
    SE = list(map(int, input().split()))
    Quantity = Quantity - SE[0] + SE[1]
    if Quantity > C:
        print("S")
        sys.exit()

print("N")
