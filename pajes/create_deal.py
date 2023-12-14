import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Create_deal(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'

    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver

    # Locators
    CRM = (By.XPATH, "//a[@href='/crm/deal/?redirect_to']")
    create_deal = (By.XPATH, "//span[text() = 'Создать']")
    name = (By.XPATH, "//input[@id='title_text']")
    user_1 = (By.XPATH, "//input[@placeholder='Имя контакта, телефон или e-mail']")
    add_goods = (By.XPATH, "//span[@class='ui-entity-editor-product-summary-empty-list-title']")
    goods_name = (By.XPATH, "//input[@data-name='NAME']")
    user_name = (By.XPATH, "//input[@id='login']")
    password = (By.XPATH, "//input[@id='password']")
    button_next = (By.XPATH, "//button[@class='ui-btn ui-btn-md ui-btn-success ui-btn-round b24-network-auth-form-btn']")
    user = (By.XPATH, "//div[@data-user-id='48671388']")
    chose_user = (By.XPATH, "//div[@data-action='open']")
    submit = (By.XPATH, "//button[@data-action='submit']")
    # Methods
    def create_deals(self):
        self.iframe()
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.get("https://becbt.bitrix24.ru/crm/deal/kanban/category/4/?current_fieldset=SOCSERV")
        self.click(self.chose_user)
        self.input(self.password, "*")
        self.click(self.submit)
        self.click(self.create_deal)
        self.iframe()
        self.input(self.name, "name")
        self.input(self.user_1, "*")
        self.click(self.add_goods)
        self.input(self.goods_name, "items")

        time.sleep(4)
