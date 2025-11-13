produkti = {'яблоки' : 52,
            'ананасы' : 100,
            'кокосы' : 150,
            'бананы' : 70}

min_cena = min(produkti, key=produkti.get)
max_cena = max(produkti, key=produkti.get)
print('продукты с минимальной ценой:', min_cena)
print('продукты с максимальной ценой:', max_cena)