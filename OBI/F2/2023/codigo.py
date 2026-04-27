N = int(input())
arquivo = input()

count = 1
for i in range(len(arquivo) - 1):
    if arquivo[i] == arquivo[i + 1]:
        count += 1
    else:
        print(f"{count} {arquivo[i]} ", end="")
        count = 1

print(f"{count} {arquivo[-1]}")
