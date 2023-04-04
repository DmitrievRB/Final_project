class Setting:
    BASE_URL = "https://b2c.passport.rt.ru/"

    VALID_EMAIL = "odi1roman@yandex.ru"
    VALID_PHONE = "+79789897112"
    VALID_LOGIN = "hhjob1"
    VALID_PASSWORD = "J2J-Nqq-ZrS-vCb"
    CONFIRM_VALID_PASSWORD = "J2J-Nqq-ZrS-vCb"
    FIRST_NAME = "Роман"
    LAST_NAME = "Одинцов"
    POSITIVE_FIRST_NAME = ["Роман", "Ро", "Р-", "АнастасияЕкатеринаАлекфывапрук"]
    POSITIVE_LAST_NAME = ["Одинцов", "Од", "О-", "АнастасияЕкатеринаАлекфывапрук"]
    AUTH_VALID_EMAIL = "hhjob1@yandex.ru"
    PERSONAL_ACCOUNT = "rtkid_1680176528575"
    REGION = "Крым"
    REQ_ELEMENTS_REG = ["Имя", "Фамилия", "Регион", "E-mail или мобильный телефон", "Пароль", "Подтверждение пароля"]
    REQ_ELEMENTS_AUTH = ["Номер", "Почта", "Логин", "Лицевой счет"]
    PLACEHOLDER_NAME = ["Мобильный телефон", "Электронная почта", "Логин", "Лицевой счёт", "Пароль"]
    ERROR_VALIDATION = ["Длина пароля должна быть не менее 8 символов",
                        "Пароль должен содержать хотя бы одну строчную букву",
                        "Пароль должен содержать хотя бы одну заглавную букву",
                        "Пароль должен содержать хотя бы одну прописную букву",
                        "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру",
                        "Длина пароля должна быть не более 20 символов",
                        "Необходимо заполнить поле кириллицей. От 2 до 30 символов.",
                        "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в "
                        "формате example@email.ru"]
    ERROR_COFIRM_PASSWORD = ["Пароли не совпадают"]
    Number = 2
