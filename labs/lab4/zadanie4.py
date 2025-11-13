def sortirovka(x):
    try:
        return tuple(sorted(x))
    except TypeError:
        return x
a = (1,30,11,2,55,1000,52)
b = ('a','b',1,2,5,1000,10)

print('кортеж а', a)
print('отсортированный кортеж а', sortirovka(a))
print('\nкортеж b', b)
print(sortirovka(b))