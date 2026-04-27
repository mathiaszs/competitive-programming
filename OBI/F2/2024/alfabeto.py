K, N = map(int, input().split())
alfabeto = input()
mensagem = input()

if all(c in alfabeto for c in mensagem):
    print("S")

else:
    print("N")
