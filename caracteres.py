string = input('Digite uma frase: ')
reverse = ''

for i in range(len(string) - 1, -1, -1):
    reverse += string[i]

print(f'A string reversa fica: {reverse}')
