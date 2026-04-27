import sys

N, C = list(map(int, input().split()))

pessoas = 0
for i in range(N):
    S, E = list(map(int, input().split()))
    pessoas = pessoas - S + E
    if pessoas > C:
        print("S")
        sys.exit()

print("N")
