import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    url = 'http://users.bugred.ru/'
    url_course = '*'
    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver


    # Locators
    login = (By.XPATH, "//a[@href='/user/login/index.html']")
    user_name = (By.XPATH, "//input[@name='login']")
    password = (By.XPATH, "//input[@name='password']")
    submit = (By.XPATH, "//input[@value='Авторизоваться']")
    add_user = (By.XPATH, "//a[contains(text(),'Добавить пользователя')]")
    add_photo = (By.XPATH, "//input[@name='noibiz_avatar']")

    save_photo = (By.XPATH, "//input[@onclick='sendFile()']")
    area = (By.XPATH, "//label[@for='imgToSend']")
    photo_path = r'D:\testing\Becbt-online\Тестданные\1.jpg'
    # Methods
    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click(self.login)
        self.input(self.user_name, "manager@mail.ru")
        self.input(self.password, "1")
        self.click(self.submit)
        self.click(self.add_user)
        # self.driver.get(self.url_course)
        # self.click(self.add_photo)
        # self.input(self.add_photo, self.photo_path)
        # self.click(self.save_photo)
        self.add_photo_to_website(self.add_photo, self.photo_path)
        time.sleep(10)

        # photo_path = r'D:\testing\Becbt-online\Тестданные\1.jpg'
        # file_input = self.driver.find_element(By.XPATH, "//input[@name='noibiz_avatar']").send_keys(photo_path)  # Замените на фактическое имя вашего input
        # # file_input.send_keys(photo_path)
        # time.sleep(10)

