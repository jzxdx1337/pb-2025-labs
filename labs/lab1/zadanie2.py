num = int(input('введите число от 1 до 9: '))

if 1 <= num <= 9:
    print(f'таблица умножения для числа {num}: ')


    for i  in range(1,11):
        res = num * i
        print(f'{num} * {i} = {res}')
else:
        print('Введено число не от 1 до 9')