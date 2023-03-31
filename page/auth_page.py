from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import Locators
from settings import *


class AuthPage(BasePage):

    def click_tab_email(self):
        # Клик по табу почта
        tab_email = self.find_element(Locators.auth_tab_email)
        tab_email.click()
        return tab_email

    def click_tab_phone(self):
        # Клик по табу телефон
        tab_phone = self.find_element(Locators.auth_tab_phone)
        tab_phone.click()
        return tab_phone

    def click_tab_login(self):
        # Клик по табу логин
        tab_login = self.find_element(Locators.auth_tab_login)
        tab_login.click()
        return tab_login

    def click_tab_personal_account(self):
        # Клик по табу Лицевой счёт
        tab_personal_account = self.find_element(Locators.auth_tab_ls)
        tab_personal_account.click()
        return tab_personal_account

    def content_left_page(self):
        # Получение левой части блока формы авторизации
        left_page = self.find_element(Locators.auth_page_left)
        return left_page

    def content_right_page(self):
        # Получение правой части блока формы авторизации
        righ_page = self.find_elements(Locators.auth_page_right)
        elements = "".join([x.text for x in righ_page])
        return elements

    def auth_placeholders(self):
        # Получение списка плейсхолдеров формы авторизации
        auth_placeholders = self.find_elements(Locators.placeholder_name)
        auth_placeholders = [x.text for x in auth_placeholders]
        return auth_placeholders

    def auth_enter_email(self):
        # Введение почты в форму авторизации
        login_email = self.find_element(Locators.auth_login)
        login_email.click()
        login_email.send_keys(Setting.AUTH_VALID_EMAIL)
        return login_email

    def auth_enter_phone(self):
        # Введение телефона в форму авторизации
        login_phone = self.find_element(Locators.auth_login)
        login_phone.click()
        login_phone.send_keys(Setting.VALID_PHONE)
        return login_phone

    def auth_enter_login(self):
        # Введение логина в форму авторизации
        login_login = self.find_element(Locators.auth_login)
        login_login.click()
        login_login.send_keys(Setting.VALID_LOGIN)
        return login_login

    def auth_enter_personal_account(self):
        # Введение лицевого счёта в форму авторизации
        auth_personal_account = self.find_element(Locators.auth_login)
        auth_personal_account.click()
        auth_personal_account.send_keys(Setting.PERSONAL_ACCOUNT)
        return auth_personal_account

    def auth_enter_password(self):
        # Введение пароля в форму авторизации
        auth_password = self.find_element(Locators.auth_password)
        auth_password.click()
        auth_password.send_keys(Setting.VALID_PASSWORD)
        return auth_password

    def auth_click_enter(self):
        # Нажатие кнопки "Войти" в форме авторизации
        auth_enter = self.find_element(Locators.auth_btn_enter)
        auth_enter.click()
        return auth_enter
