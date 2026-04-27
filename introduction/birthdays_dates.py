N = int(input())

birthdays = []

for _ in range(N):
    ent = list(map(int, input().split()))
    birthdays.append(ent)

birthdays.sort(key=lambda x: (x[1], x[0], x[2]))

print(birthdays)
