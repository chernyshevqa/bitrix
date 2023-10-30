import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'
    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver


    # Locators
    user_name = "//input[@id='login']"
    password = "//input[@id='password']"
    button_next = "//button[@class='ui-btn ui-btn-md ui-btn-success ui-btn-round b24-network-auth-form-btn']"
    user = "//div[@data-user-id='48671388']"


    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_next)))

    def get_user(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user)))


    #Action
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input password")

    def click_button_next(self):
        self.get_button_next().click()
        print("click login button")

    def click_enter(self):
        self.get_user_name().send_keys(Keys.ENTER)
        print("click enter")

    def click_user(self):
        self.get_user().click()
        print("click user")

    # Methods
    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.input_user_name("79052547785")
        time.sleep(1)
        self.click_enter()
        self.input_password("lat4Parrr")
        self.click_button_next()
        time.sleep(2)
        self.click_user()
        self.input_password("lat4Parrr")
        self.click_button_next()

        time.sleep(4)