import sys

A = int(input())
B = int(input())
C = int(input())
D = int(input())

diff1 = C - A
diff2 = C - B

# diff1 é maior

multiplos = []

i = 1
while True:

    hihi = D * i
    if hihi > C:
        break

    multiplos.append(hihi)
    i += 1

for m in multiplos:

    if m >= diff2 and m <= diff1:
        print("S")
        sys.exit()

print("N")
