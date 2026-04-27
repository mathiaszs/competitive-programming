E = int(input())
S = int(input())
L = int(input())

m1 = max(E, S)
min1 = min(E, S)
d1 = m1 - min1

m2 = max(L, S)
min2 = min(L, S)
d2 = m2 - min2

m3 = max(L, E)
min3 = min(L, E)
d3 = m3 - min3

print(d1 + d2 + d3)
