month = int(input('вести номер месяца (1-12): '))

if month < 1 or month > 12:
    print('введено число не от 1 до 12')

else:
    if month in [12,1,2]:
        vg = 'зима'
    elif month in [3,4,5]:
        vg = 'весна'
    elif month in [6,7,8]:
        vg = 'лето'
    else:
        vg = 'осень'

    print(f'{month} месяц относится к времени года {vg}')