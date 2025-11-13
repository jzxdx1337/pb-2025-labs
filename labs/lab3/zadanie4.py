num = input('ввести число: ')

ld = int(num[-1])
dsum = sum(int(cifra) for cifra in num)

if ld % 2 == 0 and dsum % 3 == 0:
    print(f'число {num} делится на 6')
else:
    print(f'число {num} не делится на 6')