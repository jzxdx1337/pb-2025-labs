def calculate_profit(a, n):
    # процент от суммы
    sum_percent = min((a // 10000) * 0.3, 5)

    # процент от срока
    if n <= 3:
        term_percent = 3
    elif n <= 6:
        term_percent = 5
    else:
        term_percent = 2

    # общий процент
    total_percent = sum_percent + term_percent

    # итоговая сумма с процентом
    total_amount = a
    for year in range(n):
        total_amount *= (1 + total_percent / 100)

    # прибыль
    profit = total_amount - a

    return profit



a = int(input('ввести сумму вклада (минимум 30000): '))
n = int(input('на какой срок делается вклад: '))
result = calculate_profit(a, n)
print(f"Прибыль: {result:.2f} рублей")