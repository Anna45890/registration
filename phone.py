print("-------РЕГИСТРАЦИЯ-------")
attempt = 0
# пользователи
user = {
    "Anna": {
        "pass": "123456",
        "level": "админ",
    },
    "Anton": {
        "pass": "654321",
        "level": "пользователь"
    },
    "Lisa": {
        "pass": "876543",
        "level": "гость"
    }
}
yes = []
# основной бесконечный цикл
while True:
    print("\n---действия---")
    print("1. Войти в аккаунт.")
    print("2. Создать аккаунт.")
    print("3. Показать всех пользователей")
    print("*Enter - назад")
    # внутренний цикл для обработки выбора
    while True:
        try:
            # получение ввода пользователя
            choice = input("\n-Выберите действие: ").strip()
            if choice == "":
                break
            choice = int(choice)
            # обработка неверного ввода
        except ValueError:
            print("Введите число!")
            continue
        if choice < 1 or choice > 3:
            print("нет такого действия.")
            continue

        # обработка выбора
        elif choice == 1:
            print("\n--ВОЙТИ В АККАУНТ--")
            while True:
                name = input("-Введите имя пользователя: ").strip().capitalize()

                if name == "":
                    break

                elif name not in user:
                    print("Пользователь не найден.")
                    continue

                elif name in user:
                    while attempt < 3:
                        attempt += 1
                        pass_user = input("-Введите пароль от аккаунта: ")
                        if user[name]["pass"] == pass_user:
                            print("\nВерный пароль")
                            print(f"Уровень доступа: {user[name]["level"]}", end='\n\n')
                            attempt -= attempt
                            if user[name]["level"] == "пользователь" or user[name]["level"] == "гость":
                                break
                            else:
                                print("---МЕНЮ АДМИНА---")
                                while True:
                                    print("\n---действия---")
                                    print("1. Создать аккаунт.")
                                    print("2. Показать всех пользователей")
                                    print("3. Удалить аккаунт")
                                    print("*Enter - назад")
                                    while True:
                                        try:
                                            # получение ввода пользователя
                                            choice = input("\n-Выберите действие: ").strip()
                                            if choice == "":
                                                break
                                            choice = int(choice)
                                            # обработка неверного ввода
                                        except ValueError:
                                            print("Введите число!")
                                            continue
                                        if choice < 1 or choice > 3:
                                            print("нет такого действия.")
                                            continue

                                        elif choice == 1:
                                            print("\n--СОЗДАТЬ АККАУНТ--")
                                            print("* Enter - назад")
                                            while True:
                                                name = input("-Введите ник: ").strip().capitalize()
                                                n = len(name)
                                                if name in user:
                                                    print(f"Плдьзователь с ником '{name}' уже есть.")
                                                    continue
                                                if name == "":
                                                    break
                                                elif n < 3:
                                                    print("Ник должно содержать больше 3 символов.")
                                                    continue
                                                while True:
                                                    pass_ = input("-Введите пароль: ").strip()
                                                    if pass_ == "":
                                                        break
                                                    s = len(pass_)
                                                    if s < 6:
                                                        print("Пароль должен содержать больше 6 символов.")
                                                        continue
                                                    else:
                                                        user[name] = {
                                                            "pass": pass_,
                                                            "level": ""
                                                        }
                                        elif choice == 2:
                                            print("\n--ВСЕ АККАУНТЫ--")
                                            if not user:
                                                print("Сервер пуст.")
                                            else:
                                                for i in user.keys():
                                                    print(i)


                                        elif choice == 3:
                                            while yes != "Да":
                                                name = input("\n-Введите ник полльзователя которого хотите удалить: ").strip().capitalize()
                                                if name == "":
                                                    break
                                                elif name not in user:
                                                    print(f"Нет пользователя с ником {name}.")
                                                    continue
                                                elif name in user:
                                                    while True:
                                                        yes = input(f"\n-Вы уверенны что хотиите удалить аккаунт {name}?: ").strip().capitalize()
                                                        if yes != "Нет" and yes != "Да":
                                                            print("Нет такого действия.")
                                                            continue
                                                        if yes == "Нет":
                                                            break
                                                        elif yes == "Да":
                                                            del user[name]
                                                            print(f"Вы удалили аккаунт {name}")
                                                            break
                                                        break
                                                        




                        elif user[name]["pass"] != pass_user:
                            print(f"Пароль неверный. Количество попыток: {3 - attempt}.")
                            continue
                    else:
                        attempt -= 3
                        print("У вас закончились попытки.")
                        break

        elif choice == 2:
            print("\n--СОЗДАТЬ АККАУНТ--")
            print("* Enter - назад")
            while True:
                name = input("-Введите ник: ").strip().capitalize()
                n = len(name)
                if name in user:
                    print(f"Плдьзователь с ником '{name}' уже есть.")
                    continue
                if name == "":
                    break
                elif n < 3:
                    print("Ник должно содержать больше 3 символов.")
                    continue
                while True:
                    pass_ = input("-Введите пароль: ").strip()
                    if pass_ == "":
                        break
                    s = len(pass_)
                    if s < 6:
                        print("Пароль должен содержать больше 6 символов.")
                        continue
                    else:
                        user[name] = {
                            "pass": pass_,
                            "level": ""
                        }


        elif choice == 3:
            print("\n--ВСЕ АККАУНТЫ--")
            if not user:
                print("Сервер пуст.")
            else:
                for i in user.keys():
                    print(i)