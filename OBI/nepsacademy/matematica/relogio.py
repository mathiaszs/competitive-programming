H = int(input())
M = int(input())
S = int(input())
T = int(input())

tempo = H * 3600
tempo += M * 60
tempo += S
tempo += T

tempo = tempo % 86400

H1 = tempo // 3600
sobra01 = tempo % 3600
M1 = sobra01 // 60
sobra02 = sobra01 % 60
S1 = sobra02 % 60

print(H1)
print(M1)
print(S1)

a = 0
