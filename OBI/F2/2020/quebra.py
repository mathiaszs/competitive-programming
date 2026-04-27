N = int(input())
entrada01 = map(int, input().split())
entrada02 = map(int, input().split())

M = []
M[0] = entrada01[0]
M[1] = entrada02[0]

for c, (i, j) in enumerate(zip(entrada01, entrada02)):
    x[0][c] = i
    x[1][c] = j

