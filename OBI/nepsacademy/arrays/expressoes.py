N = int(input())

for _ in range(N):
    S = input()
    e1, e2, e3 = 0, 0, 0

    real = 1

    for i in S:
        if i == '{':
            e1 += 1
        elif i == '}':
            e1 -= 1
            if e1 < 0:
                print("N")
                real = 0
                break

        elif i == '[':
            e2 += 1
        elif i == ']':
            e2 -= 1
            if e2 < 0:
                print("N")
                real = 0
                break

        elif i == '(':
            e3 += 1
        elif i == ')':
            e3 -= 1
            if e3 < 0:
                print("N")
                real = 0
                break

    if real == 1:
        if e1 == 0 and e2 == 0 and e3 == 0:
            print("S")
        else:
            print("N")
