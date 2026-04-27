text = ''

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        text += line
        if len(line) >= 7:
            if line[0:7] == '.......':
                break

print(text)
