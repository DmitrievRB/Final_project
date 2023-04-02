import pytest
from page.locators import Locators
from page.select_page import SelectPage
from settings import *
from time import sleep


@pytest.mark.reg
# @pytest.mark.skip
def test_check_elements_reg_form(browser):
    # HBCPRR-2 Наличие обязательных элементов в правом блоке формы регистрации
    rt_reg_page = SelectPage(browser)
    rt_reg_page.go_to_site()
    rt_reg_page.click_link_reg()
    elements = rt_reg_page.check_right_elem_reg()
    assert Setting.REQ_ELEMENTS_REG == elements


@pytest.mark.reg
# @pytest.mark.skip
def test_reg_content_left_page(browser):
    # HBCPRR-14 Содержимое левого блока формы регистрации
    rt_reg_page = SelectPage(browser)
    rt_reg_page.go_to_site()
    rt_reg_page.click_link_reg()
    rt_reg_page.check_left_elem_reg()
    assert "Персональный помощник в цифровом мире Ростелекома" in rt_reg_page.find_element(
        Locators.reg_left_elements).text


@pytest.mark.reg
# @pytest.mark.skip
@pytest.mark.parametrize("first_name, expected_first", [
    ("Роман", "Случайное имя"),
    ("Ро", "Имя из двух символов"),
    ("Р-", "Символ и тире"),
    ("АнастасияЕкатеринаАлекфывапрук", "Имя из 30 символов")],
                         ids=["fName", "f2symbol", "fSymbol-", "f30symbol"])
@pytest.mark.parametrize("last_name,expected_last", [
    ("Одинцов", "Случайная фамилия"),
    ("Од", "Фамилия из 2 символов"),
    ("О-", "фамилия символ и тире"),
    ("АнастасияЕкатеринаАлекфывапрук", "Фамилия из 30 символов")],
                         ids=["lName", "l2symbol", "lSymbol-", "l30symbol"])
@pytest.mark.parametrize("valid_phone_email,expected_login", [
    (Setting.VALID_PHONE, "Телефон формата +7ХХХХХХХХХХ"),
    (Setting.VALID_EMAIL, "Email формата example@email.ru")],
                         ids=["Valid_Phone", "Valid_Name"])
@pytest.mark.parametrize("valid_password", [Setting.VALID_PASSWORD, ], ids=["Valid_Password"])
@pytest.mark.parametrize("confirm_valid_password", [Setting.CONFIRM_VALID_PASSWORD, ],
                         ids=["Confirm_Valid_Password"])
def test_reg_user_valid_email(browser, first_name, last_name, valid_phone_email,
                              valid_password, confirm_valid_password, expected_login, expected_last, expected_first):
    # HBCPRR-1 Регистрация пользователя по телефону с валидными данными
    # HBCPRR-3 Регистрация пользователя по email с валидными данными
    # HBCPRR-15 Регистрация пользователя  с валидными данными имени
    # HBCPRR-16 Регистрация пользователя  с валидными данными фамилии.
    page = SelectPage(browser)
    page.go_to_site()
    page.click_link_reg()
    page.enter_first_name_reg(first_name)
    page.enter_last_name_reg(last_name)
    page.enter_phone_email_reg(valid_phone_email)
    page.enter_password_reg(valid_password, confirm_valid_password)
    page.click_btn_reg()
    sleep(5)
    assert "Подтверждение" in page.find_element(Locators.reg_confirm).text


@pytest.mark.auth
@pytest.mark.xfail(reason="телефон и логин не авторизованы отсюда и падение")
# @pytest.mark.skip
@pytest.mark.parametrize("valid_login_date",
                         [Setting.VALID_PHONE, Setting.AUTH_VALID_EMAIL, Setting.VALID_LOGIN, Setting.PERSONAL_ACCOUNT],
                         ids=["Valid_Phone", "Valid_Email", "Valid_Login", "Personal_Account"])
@pytest.mark.parametrize("valid_password", [Setting.VALID_PASSWORD, ], ids=["Valid_Password"])
def test_auth_user_valid_email(browser, valid_login_date, valid_password):
    # HBCPRR-4 Авторизация пользователя по почте с валидными данными
    # HBCPRR-9 Авторизация пользователя по телефону с валидными данными
    # HBCPRR-10 Авторизация пользователя по логину с валидными данными
    # HBCPRR-11 Авторизация пользователя по лицевому счету с валидными данными
    page = SelectPage(browser)
    page.go_to_site()
    page.auth_enter_login_data(valid_login_date)
    page.auth_enter_password(valid_password)
    page.auth_click_enter()
    sleep(3)
    assert page.find_element(Locators.private_cabinet).text == "Личный кабинет"
    page.auth_click_quit()


@pytest.mark.auth
@pytest.mark.skip
def test_auth_content_left_page(browser):
    # HBCPRR-12 Содержимое левого блока формы авторизации
    page = SelectPage(browser)
    page.go_to_site()
    page.auth_content_left_page()
    assert "Персональный помощник в цифровом мире Ростелекома" in page.find_element(Locators.auth_page_left).text


@pytest.mark.auth
@pytest.mark.skip
def test_auth_content_right_page(browser):
    # HBCPRR-13 Содержимое правого блока формы авторизации
    page = SelectPage(browser)
    page.go_to_site()
    elements = page.auth_content_right_page()
    page.auth_click_tab_email()
    placeholder_email = page.auth_placeholders()
    page.auth_click_tab_phone()
    placeholder_phone = page.auth_placeholders()
    page.auth_click_tab_login()
    placeholder_login = page.auth_placeholders()
    page.auth_click_tab_personal_account()
    placeholder_personal_account = page.auth_placeholders()
    assert placeholder_personal_account[0] in Setting.PLACEHOLDER_NAME
    assert placeholder_login[0] in Setting.PLACEHOLDER_NAME
    assert placeholder_phone[0] in Setting.PLACEHOLDER_NAME
    assert placeholder_email[0] in Setting.PLACEHOLDER_NAME
    assert placeholder_email[1] in Setting.PLACEHOLDER_NAME
    assert "Номер" in elements
    assert "Почта" in elements
    assert "Логин" in elements
    assert "Лицевой счёт" in elements
