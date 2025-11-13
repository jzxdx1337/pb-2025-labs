lim = int(input('число до которого будут выведены числа Фибоначчи: '))
a, b = 0, 1

while a <= lim:
    print(a)
    a, b = b, a + b