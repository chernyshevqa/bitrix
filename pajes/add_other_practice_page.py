import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base

"""Главная страница сайта"""


class Add_practise(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'

    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver

    add_courses = (By.XPATH, "//button[@class='button_ok openAddCourse']")
    add_practice = (By.XPATH, "//button[@id='addModule']")
    module_name = (By.XPATH, "//input[@id='nameModule']")
    module_type = (By.XPATH, "//select[@id='typeModule']")
    module_price = (By.XPATH, "//input[@id='amountModule']")
    module_academic_hour = (By.XPATH, "//input[@id='academicHourModule']")
    module_start_date = (By.XPATH, "//input[@id='dateStartModule']")
    module_stop_date = (By.XPATH, "//input[@id='dateStopModule']")
    module_materials_link = (By.XPATH, "//input[@id='linkMaterialsModule']")
    module_type_seminar = (By.XPATH, "//select[@id='seminarType']")
    address_of_event = (By.XPATH, "//input[@id='workshopAddress']")
    module_description = (By.XPATH, "//input[@id='descriptionModule']")
    module_checkbox_NoSendEmail = (By.XPATH, "//input[@id='noAutoMail']")
    module_speaker = (By.XPATH, "//select[@id='spicerGuid']")
    add_practice_finish = (By.XPATH, "//button[@id='ProdSave']")
    button_add_speaker = (By.XPATH, "//button[@id='addSpiker']")
    # name_of_practice = (By.XPATH, "(//p[contains(text(),'семинар 1')])[1]")
    quantity = (By.XPATH, "//input[@id='quantity']")
    button_save = (By.XPATH, "//button[@id='ProdSave']")

    def iframe(self):
        return WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='app-frame']")))

    def test_add_practice(self):
        self.click(self.add_practice)
        self.select_option_by_visible_text(self.module_type, "ТиНы")
        self.input(self.module_price, "100")
        self.clear_value_fields(self.quantity)
        self.input(self.quantity, "10")
        self.click(self.button_save)
        self.check_practice("ТиНы")
