verify = int(input('Qual número você deseja verificar se pertence a sequência?: '))

fibonnaciCounterOne, fibonnaciCounterTwo = 0, 1

result = f'{fibonnaciCounterOne} 🠒 {fibonnaciCounterTwo} 🠒 '

while fibonnaciCounterTwo <= verify:
    if fibonnaciCounterTwo == verify:
        result += f'Pertence a sequência.'
        break

    fibonnaciCounterThree = fibonnaciCounterOne + fibonnaciCounterTwo
    result += f'{fibonnaciCounterThree} 🠒 '

    fibonnaciCounterOne = fibonnaciCounterTwo
    fibonnaciCounterTwo = fibonnaciCounterThree

if fibonnaciCounterTwo > verify:
    result += f'O número não pertence a sequência.'

print(result)