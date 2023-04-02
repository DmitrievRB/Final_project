# Final_project

Отчет о проделанном тестировании

В рамках данного проекта было проведено тестирование методом черного ящика. Целью тестирования была проверка
функциональности и корректности работы системы авторизации и регистрации пользователей. Для тестирования были
использованы следующие инструменты и техники:

- PyCharm - среда разработки для написания и запуска тестов на языке Python
- tests.py - файл, содержащий набор тестовых сценариев для проверки различных аспектов системы
- классы эквивалентности и граничные значения - техники, позволяющие определить минимальное количество тестовых данных
  для покрытия всех возможных вариантов ввода и вывода
- элементы системы - объекты интерфейса, с которыми взаимодействует пользователь (поля, чекбоксы, кнопки и т.д.)
- логика работы системы - правила и алгоритмы, определяющие поведение системы в зависимости от входных данных и условий
- бизнес-процесс - последовательность действий пользователя для достижения определенной цели в системе

В ходе тестирования были проверены следующие сценарии:

- позитивные тесты на авторизацию через: телефон, email, логин. Тесты проверяли успешный вход в систему при вводе
  корректных данных в поле username и пароль
- тест на проверку надписи в поле ввода при переключении режимов ввода username. Тест проверял соответствие надписи "
  Введите номер телефона", "Введите email" или "Введите логин" при выборе соответствующего режима
- тесты на проверку наличия и функционирование кнопок авторизации через соцсети. Тесты проверяли отображение кнопок "
  Войти через Facebook", "Войти через Google" и "Войти через VK" на странице авторизации и переход на страницу
  соответствующей соцсети при нажатии на них
- тест на проверку наличия error сообщений на странице регистрации при введении пустых полей. Тест проверял появление
  сообщений "Поле обязательно для заполнения" под каждым пустым полем при нажатии на кнопку "Зарегистрироваться"
- тест на проверку функционирования поля "Проверка пароля" на странице регистрации. Тест проверял совпадение значений в
  полях "Пароль" и "Проверка пароля" при вводе одинаковых или разных паролей
- тесты на проверку ввода в поле "Пароль" на странице регистрации согласно парольной политике. Тесты проверяли принятие
  или отклонение паролей разной длины и содержания (буквы, цифры, спецсимволы) и появление сообщений "Пароль должен быть
  не менее 8 символов", "Пароль должен содержать хотя бы одну цифру" или "Пароль должен содержать хотя бы один
  спецсимвол"
- тесты на проверку ввода не валидного телефона/email в поле username и появления error сообщения. Тесты проверяли
  отклонение телефонов или email с неправильным форматом или символов

python -m pytest -v --driver Chrome --driver-path \driver\chromedriver.exe tests\test_positive.py


