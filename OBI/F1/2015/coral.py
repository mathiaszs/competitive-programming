entrada = list(map(int, input().split()))
A, B, C, D = entrada[0], entrada[1], entrada[2], entrada[3]

if A == C or B == D:
    print("V")
else:
    print("F")
