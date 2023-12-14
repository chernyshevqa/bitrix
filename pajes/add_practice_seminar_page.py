import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from test_data.data_test import *



class Add_practise(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'

    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver

    name_of_practice = date_for_seminar["date_seminar_name"]
    name_of_seminar = (By.XPATH, f"(//p[contains(text(),'{name_of_practice}')])[1]")
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



    # def iframe(self):
    #     return WebDriverWait(self.driver, 30).until(
    #         EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='app-frame']")))

    def practise_add(self):
        with allure.step("создание практики"):
            self.click(self.add_practice)
            time.sleep(2)
            self.input(self.module_name, self.name_of_practice)
            self.select_option_by_visible_text(self.module_type, "Семинар")
            self.input(self.module_price, date_for_seminar['date_module_price'])
            self.input(self.module_academic_hour, date_for_seminar['date_module_academic_hour'])
            self.input(self.module_start_date, date_for_seminar['date_module_start_date'])
            self.input(self.module_stop_date, date_for_seminar['date_module_stop_date'])
            self.input(self.module_materials_link, date_for_seminar['date_module_materials_link'])
            self.select_option_by_visible_text(self.module_type_seminar, "online")
            self.input(self.address_of_event, date_for_seminar['date_address_of_event'])
            self.input(self.module_description, date_for_seminar['date_module_description'])
            self.select_option_by_visible_text(self.module_speaker, "Семчанко Софья Владимирована")
            self.click(self.button_add_speaker)
            time.sleep(2)
            self.click(self.add_practice_finish)
            self.check_practice(self.name_of_practice)
