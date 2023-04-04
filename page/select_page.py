from .base_page import BasePage
from .locators import Locators
from settings import *


class SelectPage(BasePage):
    def __init__(self, driver, timeout=25):
        super().__init__(driver, timeout)

    def click_link_reg(self):
        # Нажатие на ссылку зарегистрироваться
        reg_link = self.find_element(Locators.reg_link)
        reg_link.click()
        return reg_link

    def check_right_elem_reg(self):
        # Получение элементов правого блока форме регистрации
        all_reg_elements = self.find_elements(Locators.reg_right_elements)
        elements = [x.text for x in all_reg_elements]
        return elements

    def check_left_elem_reg(self):
        # Получение элементов левого блока форме регистрации
        elements = self.find_elements(Locators.reg_left_elements)
        return elements

    def enter_first_name_reg(self, first_name):
        # Передаем значение в поле ввода имя
        name = self.find_element(Locators.reg_first_name)
        name.send_keys(first_name)
        return name

    def enter_last_name_reg(self, first_name):
        # Готовим поле для фамилии в форме регистрации
        name = self.find_element(Locators.reg_last_name)
        name.send_keys(first_name)
        return name

    def enter_phone_email_reg(self, phone_email):
        # Готовим поле для ввода номера телефона или почты
        email = self.find_element(Locators.reg_mail_phone)
        email.send_keys(phone_email)
        return email

    def enter_password_reg(self, reg_password, reg_confirm_password):
        # Передаем значение в поле ввода пароля и подтверждения
        password = self.find_element(Locators.reg_password)
        password.click()
        password.send_keys(reg_password)
        confirm_password = self.find_element(Locators.reg_confirm_password)
        confirm_password.click()
        confirm_password.send_keys(reg_confirm_password)
        return password, confirm_password

    def click_btn_reg(self):
        # Нажимаем кнопку Зарегистрироваться
        btn = self.find_element(Locators.reg_btn_register)
        btn.click()
        return btn

    def enter_phone_reg(self):
        # Передаем значение в поле ввода номера телефона или почты
        phone = self.find_element(Locators.reg_mail_phone)
        phone.click()
        phone.send_keys(Setting.VALID_PHONE)
        return phone

    def auth_click_tab_email(self):
        # Клик по табу почта
        tab_email = self.find_element(Locators.auth_tab_email)
        tab_email.click()
        return tab_email

    def auth_click_tab_phone(self):
        # Клик по табу телефон
        tab_phone = self.find_element(Locators.auth_tab_phone)
        tab_phone.click()
        return tab_phone

    def auth_click_tab_login(self):
        # Клик по табу логин
        tab_login = self.find_element(Locators.auth_tab_login)
        tab_login.click()
        return tab_login

    def auth_click_tab_personal_account(self):
        # Клик по табу Лицевой счёт
        tab_personal_account = self.find_element(Locators.auth_tab_ls)
        tab_personal_account.click()
        return tab_personal_account

    def auth_content_left_page(self):
        # Получение левой части блока формы авторизации
        left_page = self.find_element(Locators.auth_page_left)
        return left_page

    def auth_content_right_page(self):
        # Получение правой части блока формы авторизации
        right_page = self.find_elements(Locators.auth_page_right)
        elements = "".join([x.text for x in right_page])
        return elements

    def auth_placeholders(self):
        # Получение списка плейсхолдеров формы авторизации
        auth_placeholders = self.find_elements(Locators.auth_placeholder_name)
        auth_placeholders = [x.text for x in auth_placeholders]
        return auth_placeholders

    def auth_enter_login_data(self, valid_login_date):
        # Введение телефона в форму авторизации
        login_phone = self.find_element(Locators.auth_login)
        login_phone.click()
        login_phone.send_keys(valid_login_date)
        return login_phone

    def auth_enter_password(self, valid_password):
        # Введение пароля в форму авторизации
        auth_password = self.find_element(Locators.auth_password)
        auth_password.click()
        auth_password.send_keys(valid_password)
        return auth_password

    def auth_click_enter(self):
        # Нажатие кнопки "Войти" в форме авторизации
        auth_enter = self.find_element(Locators.auth_btn_enter)
        auth_enter.click()
        return auth_enter

    def auth_click_quit(self):
        # Нажатие кнопки "Выход" в личном кабинете
        auth_quit = self.find_element(Locators.private_cabinet_quit)
        auth_quit.click()
        return auth_quit

    def error_reg_first_name(self):
        # Получение ошибки регистрации имени
        error_reg = self.find_element(Locators.error_fist_name)
        error = error_reg.text
        return error

    def error_reg_last_name(self):
        # Получение ошибки регистрации Фамилии
        error_reg = self.find_element(Locators.error_last_name)
        error = error_reg.text

        return error

    def error_reg_login(self):
        # Получение ошибки регистрации в почте или телефоне
        error_reg = self.find_element(Locators.error_login)
        error = error_reg.text

        return error

    def error_reg_password(self):
        # Получение ошибки регистрации в пароле
        error_reg = self.find_element(Locators.error_password)
        error = error_reg.text

        return error

    def error_reg_confirm_password(self):
        # Получение ошибки регистрации в подтверждении пароля
        error_reg = self.find_element(Locators.error_confirm_password)
        error = error_reg.text

        return error
