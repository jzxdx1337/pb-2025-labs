password = input('ввести пароль: ')


errors = []
if len(password) < 8:
    errors.append('пароль должен быть не менее 8 символов')

if not any(char.isupper() for char in password):
    errors.append('пароль должен содержать заглавные буквы')

if not any(char.islower() for char in password):
    errors.append('пароль должен содержать строчные буквы')

if not any(char.isdigit() for char in password):
    errors.append('пароль должен содержать цифры')

if not any(char.isalnum() for char in password):
    errors.append('пароль должен содержать специальные символы')

if errors:
    print('////////////////////////////////////')
    print('пароль является ненадёжным. ошибки:')
    print('///////////////////////////////////')
    for error in errors:
        print(error)
else:
    print('///////////////////////////////////')
    print('пароль надёжный')
    print('///////////////////////////////////')