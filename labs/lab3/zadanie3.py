try:
    sobaka = float(input('ввести возраст собаки: '))
    if sobaka < 1:
        print('возраст должен быть не меньше 1 года')
    elif sobaka > 22:
        print('возраст собаки не должен превышаать 22 года')
    else:
        if sobaka <= 2:
            chel = sobaka * 10.5
        else:
            chel = 2 * 10.5 + (sobaka - 2) * 4

        print(f'возраст собаки переведённый на человеческий: {chel}')
except ValueError:
    print('введено не число')