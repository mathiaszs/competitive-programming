S = int(input())
A = int(input())
B = int(input())

count = 0
x = A
while x <= B:
    sum = 0
    for i in range(len(str(x))):
        sum += int(str(x)[i])
    if sum == S:
        count += 1
    x += 1

print(count)
