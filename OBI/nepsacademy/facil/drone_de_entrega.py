A = int(input())
B = int(input())
C = int(input())
H = int(input())
L = int(input())

caixa = [A, B, C]
caixa.sort(reverse=True)
del caixa[0]
janela = [H, L]
janela.sort(reverse=True)

if caixa[0] > janela[0] or caixa[1] > janela[1]:
    print("N")
else:
    print("S")

