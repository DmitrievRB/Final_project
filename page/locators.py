from selenium.webdriver.common.by import By


class Locators:
    # Локаторы страницы регистрации
    reg_link = (By.ID, "kc-register")
    reg_title = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    reg_first_name = (By.NAME, "firstName")
    reg_last_name = (By.NAME, "lastName")
    reg_region_text = (By.XPATH, "//span[contains(text(),'Регион')]")
    reg_out_region = (By.CSS_SELECTOR, ".rt-select__list-item")
    reg_in_region = (By.XPATH,
                     "//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']")
    reg_mail_phone = (By.XPATH, "//input[@id='address']")
    reg_password = (By.XPATH, "//input[@id='password']")
    reg_confirm_password = (By.XPATH, "//input[@id='password-confirm']")
    reg_btn_register = (By.NAME, "register")
    reg_user_agreement = (By.XPATH, "//a[@href='https://b2c.passport.rt.ru/sso-static/agreement/agreement.html']")
    reg_right_elements = (By.CLASS_NAME, "rt-input--rounded")
    reg_left_elements = (By.ID, "page-left")
    reg_email_confirm = (By.XPATH, "//section/div/div/h1")
    reg_confirm = (By.XPATH, "//h1[contains(text(),'Подтверждение')]")
    error_password = (By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error")
    error_confirm_password = (By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error")

    # Локаторы страницы авторизации
    auth_tab_email = (By.XPATH, "//div[@id='t-btn-tab-mail']")
    auth_tab_phone = (By.XPATH, "//div[@id='t-btn-tab-phone']")
    auth_tab_login = (By.XPATH, "//div[@id='t-btn-tab-login']")
    auth_tab_ls = (By.XPATH, "//div[@id='t-btn-tab-ls']")
    auth_login = (By.XPATH, "//input[@id='username']")
    auth_password = (By.XPATH, "//input[@id='password']")
    auth_btn_enter = (By.XPATH, "//button[@id='kc-login']")
    auth_page_left = (By.ID, "page-left")
    auth_page_right = (By.CLASS_NAME, "rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs")
    auth_placeholder_name = (By.CLASS_NAME, "rt-input__placeholder")
    auth_placeholder_email_passw = (By.XPATH, '//span[@class="rt-input__mask-start"]')
    # Прочие страницы
    private_cabinet = (By.XPATH, "//a[@id='lk-btn']")
    private_cabinet_quit = (By.XPATH, "//div[@id='logout-btn']")
