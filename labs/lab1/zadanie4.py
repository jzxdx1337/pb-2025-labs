num = int(input('число для вычисления факториала: '))


if num < 0:
    print('факториал отрицательного числа не определен')
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i

    print(f'факториал числа {num} равен {fact}')