def convert_time(value, from_unit, to_unit):
    to_seconds = {
        's': 1,
        'm': 60,
        'h': 3600,
        'd': 86400
    }

    value_in_seconds = value * to_seconds[from_unit]

    result = value_in_seconds / to_seconds[to_unit]

    return result


def main():
    vremyas = float(input('ввести число: '))
    velichinas = input('в какую это величине: s/m/h/d: ')
    vkakie = input('в какую величину перевести: s/m/h/d: ')


    result1 = convert_time(vremyas, velichinas, vkakie)
    print(f"{vremyas}{velichinas} {vkakie} = {result1}{vkakie}")


if __name__ == "__main__":
    main()