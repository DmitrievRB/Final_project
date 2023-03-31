from .base_page import BasePage
from .locators import Locators
from settings import *


class RegistrPage(BasePage):

    def click_link_reg(self):
        reg_link = self.find_element(Locators.reg_link)
        reg_link.click()
        return reg_link

    def check_right_elem_reg(self):
        all_reg_elements = self.find_elements(Locators.reg_right_elements)
        elements = [x.text for x in all_reg_elements]
        # print(elements)
        return elements

    def check_left_elem_reg(self):
        elements = self.find_elements(Locators.reg_left_elements)
        print(elements)
        return elements

    def enter_first_name(self):
        name = self.find_element(Locators.first_name)
        name.click()
        name.send_keys(Setting.FIRST_NAME)
        return name

    def enter_last_name(self):
        name = self.find_element(Locators.last_name)
        name.click()
        name.send_keys(Setting.LAST_NAME)
        return name

    def enter_email(self):
        email = self.find_element(Locators.reg_mail_phone)
        email.click()
        email.send_keys(Setting.VALID_EMAIL)
        return email

    def enter_password_reg(self):
        password = self.find_element(Locators.reg_password)
        password.click()
        password.send_keys(Setting.VALID_PASSWORD)
        confirm_password = self.find_element(Locators.confirm_password)
        confirm_password.click()
        confirm_password.send_keys(Setting.REPET_VALID_PASSWORD)
        return password, confirm_password

    def click_btn_reg(self):
        btn = self.find_element(Locators.btn_register)
        btn.click()
        return btn

    def enter_phone(self):
        phone = self.find_element(Locators.reg_mail_phone)
        phone.click()
        phone.send_keys(Setting.VALID_PHONE)
        return phone
