import pytest
from page.select_page import SelectPage
from settings import *
from time import sleep


@pytest.mark.parametrize("first_name", ["", "012", "Sasha", "北京位於華", "Ффффффффффффффффффффффффффффффыыыыыыы"],
                         ids=["fNull", "fNumber", "fLatin", "Chinese", "31symbol"])
def test_reg_user_invalid_first_name(browser, first_name, last_name=Setting.LAST_NAME,
                                     phone_email=Setting.VALID_PHONE,
                                     valid_password=Setting.VALID_PASSWORD,
                                     confirm_valid_password=Setting.CONFIRM_VALID_PASSWORD):
    # HBCPRR-17 Регистрация с невалидными данными имени.
    page = SelectPage(browser)
    page.go_to_site()
    page.click_link_reg()
    page.enter_first_name_reg(first_name)
    page.enter_last_name_reg(last_name)
    page.enter_phone_email_reg(phone_email)
    page.enter_password_reg(valid_password, confirm_valid_password)
    page.click_btn_reg()

    sleep(5)
    assert page.error_reg_first_name() in Setting.ERROR_VALIDATION


@pytest.mark.parametrize("last_name", ["", "012", "Sasha", "北京位於華", "Ффффффффффффффффффффффффффффффыыыыыыы"],
                         ids=["fNull", "fNumber", "fLatin", "Chinese", "31symbol"])
def test_reg_user_invalid_last_name(browser, last_name, phone_email=Setting.VALID_PHONE,
                                    first_name=Setting.FIRST_NAME,
                                    valid_password=Setting.VALID_PASSWORD,
                                    confirm_valid_password=Setting.CONFIRM_VALID_PASSWORD):
    # HBCPRR-18 Регистрация с невалидными данными фамилии.
    page = SelectPage(browser)
    page.go_to_site()
    page.click_link_reg()
    page.enter_first_name_reg(first_name)
    page.enter_last_name_reg(last_name)
    page.enter_phone_email_reg(phone_email)
    page.enter_password_reg(valid_password, confirm_valid_password)
    page.click_btn_reg()

    sleep(5)
    assert page.error_reg_last_name() in Setting.ERROR_VALIDATION


@pytest.mark.parametrize("phone_email", ["", "sasha@mail", "sashamail.ru", "sa sha@mail.ru", "саша@почта.рф",
                                         "+790382222344", "+7903_903903", "+7903z903903", "+7903903903"],
                         ids=["isNull", "sasha@mail", "sashamail.ru", "sa sha@mail.ru", "саша@почта.рф",
                              "+7ххххххххххx", "+7ххх_хххххх", "+7хххzхххххх", "+7ххххххххх"])
def test_reg_user_invalid_login(browser, phone_email, last_name=Setting.FIRST_NAME, first_name=Setting.FIRST_NAME,
                                valid_password=Setting.VALID_PASSWORD,
                                confirm_valid_password=Setting.CONFIRM_VALID_PASSWORD):
    # HBCPRR-19 Регистрация с невалидными данными почты.
    # HBCPRR-20 Регистрация с невалидными данными телефона.

    page = SelectPage(browser)
    page.go_to_site()
    page.click_link_reg()
    page.enter_first_name_reg(first_name)
    page.enter_last_name_reg(last_name)
    page.enter_phone_email_reg(phone_email)
    page.enter_password_reg(valid_password, confirm_valid_password)
    page.click_btn_reg()

    sleep(5)
    assert page.error_reg_login() in Setting.ERROR_VALIDATION


@pytest.mark.parametrize("reg_password", ["", "Aa34567", "aa345678", "AA345678", "AAsdfghj", Setting.Number * 255],
                         ids=["isNull", ">8", "lower", "upper", "NotNumber", "255symbol"])
def test_reg_user_invalid_password(browser, reg_password, last_name=Setting.FIRST_NAME,
                                   first_name=Setting.FIRST_NAME,
                                   phone_email=Setting.VALID_PHONE,
                                   reg_confirm_password=Setting.CONFIRM_VALID_PASSWORD):
    page = SelectPage(browser)
    page.go_to_site()
    page.click_link_reg()
    page.enter_first_name_reg(first_name)
    page.enter_last_name_reg(last_name)
    page.enter_phone_email_reg(phone_email)
    page.enter_password_reg(reg_password, reg_confirm_password)
    page.click_btn_reg()

    sleep(5)
    assert page.error_reg_password() in Setting.ERROR_VALIDATION


@pytest.mark.parametrize("reg_confirm_password",
                         ["", "Aa34567", "aa345678", "AA345678", "AAsdfghj", Setting.Number * 255, "J2J-Nqq-ZrS-vC"],
                         ids=["isNull", ">8", "lower", "upper", "NotNumber", "255symbol", "!=password"])
def test_reg_user_invalid_confirm_password(browser, reg_confirm_password, last_name=Setting.FIRST_NAME,
                                           first_name=Setting.FIRST_NAME,
                                           phone_email=Setting.VALID_PHONE,
                                           reg_password=Setting.VALID_PASSWORD):
    page = SelectPage(browser)
    page.go_to_site()
    page.click_link_reg()
    page.enter_first_name_reg(first_name)
    page.enter_last_name_reg(last_name)
    page.enter_phone_email_reg(phone_email)
    page.enter_password_reg(reg_password, reg_confirm_password)
    page.click_btn_reg()

    sleep(5)
    assert page.error_reg_confirm_password() in Setting.ERROR_COFIRM_PASSWORD
