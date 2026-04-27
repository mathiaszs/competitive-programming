def main():
    N = int(input())
    c = input()

    maior = []
    for i in range(len(c)):
        for j in range(i + 1, len(c) + 1):
            new = c[i:j]
            if palindromo(new) == True:
                maior.append(len(new))

    print(max(maior))

def palindromo(string):
    count = 0
    lenght = len(string)
    if lenght % 2 == 1:
        lenght = lenght - 1

    # Se a metade for inverso da outra metade, é palindromo
    for i in range(lenght // 2):
        if string[i] == string[-i - 1]:
            count += 1

    if count == lenght // 2:
        return True

    return False

main()

    # def palindromo(string):
    # for i in range(len(string) // 2):
    #     if string[i] != string[-i - 1]:
    #         return False
    # return True
