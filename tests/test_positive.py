from page.registr_page import RegistrPage
from page.locators import Locators
from page.auth_page import AuthPage
from settings import *
from time import sleep


def test_check_elements_reg_form(browser):
    # HBCPRR-2 Наличие обязательных элементов на странице регистрации согласно требованиям
    rt_reg_page = RegistrPage(browser)
    rt_reg_page.go_to_site()
    rt_reg_page.click_link_reg()
    elements = rt_reg_page.check_right_elem_reg()
    assert Setting.REQ_ELEMENTS_REG == elements


def test_reg_content_left_page(browser):
    # HBCPRR-14 Содержимое левого блока формы регистрации
    rt_reg_page = RegistrPage(browser)
    rt_reg_page.go_to_site()
    rt_reg_page.click_link_reg()
    rt_reg_page.check_left_elem_reg()
    assert "Персональный помощник в цифровом мире Ростелекома" in rt_reg_page.find_element(
        Locators.reg_left_elements).text


def test_reg_user_valid_email(browser):
    # HBCPRR-1 Регистрация пользователя по телефону с валидными данными
    rt_reg_page = RegistrPage(browser)
    rt_reg_page.go_to_site()
    rt_reg_page.click_link_reg()
    rt_reg_page.enter_first_name()
    rt_reg_page.enter_last_name()
    rt_reg_page.enter_email()
    rt_reg_page.enter_password_reg()
    rt_reg_page.click_btn_reg()
    assert rt_reg_page.find_element(Locators.email_confirm).text == "Подтверждение email"


def test_reg_user_valid_phone(browser):
    # HBCPRR-3 Регистрация пользователя по email с валидными данными
    rt_reg_page = RegistrPage(browser)
    rt_reg_page.go_to_site()
    rt_reg_page.click_link_reg()
    rt_reg_page.enter_first_name()
    rt_reg_page.enter_last_name()
    rt_reg_page.enter_phone()
    rt_reg_page.enter_password_reg()
    rt_reg_page.click_btn_reg()
    assert rt_reg_page.find_element(Locators.phone_confirm).text == "Подтверждение телефона"


def test_auth_user_valid_email(browser):
    # HBCPRR-4 Авторизация пользователя по почте с валидными данными
    rt_auth_page = AuthPage(browser)
    rt_auth_page.go_to_site()
    rt_auth_page.auth_enter_email()
    rt_auth_page.auth_enter_password()
    rt_auth_page.auth_click_enter()
    assert rt_auth_page.find_element(Locators.private_cabinet).text == "Личный кабинет"


def test_auth_user_valid_phone(browser):
    # HBCPRR-9 Авторизация пользователя по телефону с валидными данными
    rt_auth_page = AuthPage(browser)
    rt_auth_page.go_to_site()
    rt_auth_page.auth_enter_phone()
    rt_auth_page.auth_enter_password()
    rt_auth_page.auth_click_enter()
    assert rt_auth_page.find_element(Locators.private_cabinet).text == "Личный кабинет"


def test_auth_user_valid_login(browser):
    # HBCPRR-10 Авторизация пользователя по логину с валидными данными
    rt_auth_page = AuthPage(browser)
    rt_auth_page.go_to_site()
    rt_auth_page.auth_enter_login()
    rt_auth_page.auth_enter_password()
    rt_auth_page.auth_click_enter()
    assert rt_auth_page.find_element(Locators.private_cabinet).text == "Личный кабинет"


def test_auth_user_valid_personal_account(browser):
    # HBCPRR-11 Авторизация пользователя по лицевому счету с валидными данными
    rt_auth_page = AuthPage(browser)
    rt_auth_page.go_to_site()
    rt_auth_page.auth_enter_login()
    rt_auth_page.auth_enter_password()
    rt_auth_page.auth_click_enter()
    assert rt_auth_page.find_element(Locators.private_cabinet).text == "Личный кабинет"


def test_auth_content_left_page(browser):
    # HBCPRR-12 Содержимое левого блока формы авторизации
    rt_auth_page = AuthPage(browser)
    rt_auth_page.go_to_site()
    rt_auth_page.content_left_page()
    assert "Персональный помощник в цифровом мире Ростелекома" in rt_auth_page.find_element(
        Locators.auth_page_left).text


def test_auth_content_right_page(browser):
    # HBCPRR-13 Содержимое правого блока формы авторизации
    rt_auth_page = AuthPage(browser)
    rt_auth_page.go_to_site()
    elements = rt_auth_page.content_right_page()
    rt_auth_page.click_tab_email()
    placeholder_email = rt_auth_page.auth_placeholders()
    rt_auth_page.click_tab_phone()
    placeholder_phone = rt_auth_page.auth_placeholders()
    rt_auth_page.click_tab_login()
    placeholder_login = rt_auth_page.auth_placeholders()
    rt_auth_page.click_tab_personal_account()
    placeholder_personal_account = rt_auth_page.auth_placeholders()
    assert placeholder_personal_account[0] in Setting.PLACEHOLDER_NAME
    assert placeholder_login[0] in Setting.PLACEHOLDER_NAME
    assert placeholder_phone[0] in Setting.PLACEHOLDER_NAME
    assert placeholder_email[0] in Setting.PLACEHOLDER_NAME
    assert placeholder_email[1] in Setting.PLACEHOLDER_NAME
    assert "Номер" in elements
    assert "Почта" in elements
    assert "Логин" in elements
    assert "Лицевой счёт" in elements


def test_reg_user_valid_first_name(browser, first_name):
    first_name = Setting.FIRST_NAME
    # HBCPRR-15 Регистрация пользователя  с валидными данными имени
    rt_reg_page = RegistrPage(browser)
    rt_reg_page.go_to_site()
    rt_reg_page.click_link_reg()
    rt_reg_page.enter_last_name()
    rt_reg_page.enter_email()
    rt_reg_page.enter_password_reg()
    rt_reg_page.click_btn_reg()
    assert rt_reg_page.find_element(Locators.email_confirm).text == "Подтверждение email"


def test_region(browser):
    rt_reg_page = RegistrPage(browser)
    rt_reg_page.go_to_site()
    rt_reg_page.click_link_reg()
    rt_reg_page.enter_region()
    rt_reg_page.click_region()
    sleep(10)
    assert rt_reg_page.find_element(Locators.email_confirm).text == "Подтверждение email"
