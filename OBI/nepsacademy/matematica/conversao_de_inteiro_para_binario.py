N = int(input())

N = list(str(bin(N)))
del N[0]
del N[0]

print(*N, sep="")

a = 0
