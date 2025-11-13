name = input('введите имя: ')
age = input('введите возраст: ')

count = 1
for r in range(0,10):

    print(f'{count}. Меня зовут {name} и мне {age} лет')
    count += 1