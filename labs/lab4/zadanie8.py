import random

vibori = ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']
pravila = {
    'ножницы': ['бумага', 'ящерица'],
    'бумага': ['камень', 'спок'],
    'камень': ['ножницы', 'ящерица'],
    'ящерица': ['бумага', 'спок'],
    'спок': ['ножницы', 'камень']}

print('Доступные варианты: камень, ножницы, бумага, ящерица, спок')

while True:

    user_choice = input('Ваш выбор: ').lower()

    if user_choice not in vibori:
        print('Выберите слово из предложенных вариантов')
        continue

    computer_choice = random.choice(vibori)
    print(f'Компьютер выбрал: {computer_choice}')

    if user_choice == computer_choice:
        print('Ничья')
        break
    elif computer_choice in pravila[user_choice]:
        print('Вы победили')
        break
    else:
        print('Компьютер победил')
        break