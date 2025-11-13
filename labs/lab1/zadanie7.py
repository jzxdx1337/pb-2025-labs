strok = input('строка: ')
res = ''



for i, char in enumerate(strok,1):
    res += char + str(i)

print(res)