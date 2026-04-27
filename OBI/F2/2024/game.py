N = int(input())
a = input()

count = 1
for i in a:
    if i == "E":
        count = count * 2
    if i == "D":
        count = count * 2 + 1

print(count)
