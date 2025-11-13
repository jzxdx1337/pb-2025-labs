words = {
    'apple': 'яблоко',
    'dog': 'собака',
    'cat': 'кот',
    'car': 'машина'}

russikie = input('Введите русское слово: ').lower()
for eng, rus in words.items():
    if rus == russikie:
        print('слово на английском: ', eng)
        break
else:
    print('Такого слова в словаре нет')