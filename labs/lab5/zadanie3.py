def is_prime(n):

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def print_primes_in_range(start, end):

    if not isinstance(start, int) or not isinstance(end, int):
        print("Ошибка: начало и конец диапазона должны быть целыми числами")
        return

    if start > end:
        print("Ошибка: начало диапазона не может быть больше конца")
        return

    if start < 0 or end < 0:
        print("Ошибка: диапазон не может содержать отрицательные числа")
        return

    primes = []

    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)

    if primes:
        print(f"Простые числа в диапазоне от {start} до {end}:")
        print(primes)
    else:
        print(f"В диапазоне от {start} до {end} нет простых чисел")


start = int(input('ввести начало диапазона: '))
end = int(input('ввести конец диапазона: '))


if __name__ == "__main__":
    print_primes_in_range(start, end)
    print()