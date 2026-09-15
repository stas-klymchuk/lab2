# База даних користувачів (логін, пароль та список оцінок)
users = {
    "stas": {"password": "123", "grades": [10, 8, 3, 11, 5]},
    "anna": {"password": "456", "grades": [4, 4, 3, 5, 12]},
    "ivan": {"password": "789", "grades": [9, 10, 11, 12, 2]},
    "olga": {"password": "000", "grades": [2, 3, 4, 5, 6]}
}

print("=== СИСТЕМА АВТОРИЗАЦІЇ ===")
input_login = input("Введіть логін: ")
input_pass = input("Введіть пароль: ")

# Перевірка чи існує користувач і чи збігається пароль
if input_login in users and users[input_login]["password"] == input_pass:
    print("\nВхід успішний! Вітаємо,", input_login)

    grades_list = users[input_login]["grades"]
    print("Ваші оцінки:", grades_list)

    # Лічильники для оцінок
    satisfactory = 0  # від 5 до 12
    unsatisfactory = 0  # від 1 до 4

    for grade in grades_list:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print(f"Кількість оцінок від 5 до 12 (задовільно): {satisfactory}")
    print(f"Кількість оцінок від 1 до 4 (незадовільно): {unsatisfactory}")

else:
    print("\nПомилка: Неправильний логін або пароль!")