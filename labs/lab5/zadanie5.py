def check_palindrome():
    text = input("Введите строку: ")
    text_bez_probelov = text.replace(" ", "").lower()



    if text_bez_probelov == text_bez_probelov[::-1]:
        print("Да")
    else:
        print("Нет")


if __name__ == "__main__":
    check_palindrome()