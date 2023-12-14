# import time
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from test_data.data_test import *


"""Главная страница сайта"""
class Search_course(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'
    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver

    # Locators
    # course = "//a[text() ='Курсы']"
    name_of_course = test_date["date_course_name"]
    search = (By.XPATH, "//input[@id='name_сourse_search']")
    start_course = "//input[@id='date_start_сourse_search']"
    stop_course = "//input[@id='date_stop_сourse_search']"
    checkbox_off_filter = (By.XPATH, "//input[@id='off_search']")
    checkbox_current_courses = (By.XPATH, "//input[@id='curent_сourse_search']")
    checkbox_past_courses = (By.XPATH, "//input[@id='past_сourse_search']")
    checkbox_coming_courses = (By.XPATH, "//input[@id='coming_сourse_search']")
    checkbox_current_and_coming_courses = (By.XPATH, "//input[@id='curent_coming_сourse_search']")
    search_button = (By.XPATH, "//button[@class='button_ok сourse_search']")
    course_name = f"//span[@id='course_name'][text()=' {name_of_course}']"
    name_of_course_after_search = (By.XPATH, "//span[@id='main_title_course']")
    short_name_course = (By.XPATH, "//input[@id='shortNameCourse']")
    edit_courses = (By.XPATH, "//button[@class='button_ok openUpdateCourse']")
    button_delete_course = (By.XPATH, "//button[@id='delCourse']")
    list_of_course = (By.XPATH, "//button[@class='button_ok openGuide']")

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
    module_error = (By.XPATH, "//p[@class='mess_error_module']")
    seminar = (By.XPATH, "(//div[@class='rowTovar_main rowTovar_main_list_moduls'])[1]")

    # Getters

    def iframe(self):
        return WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='app-frame']")))

    def get_course_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.course_name)))

    def click_course_name(self):
        self.get_course_name().click()
        print("клик курс")

    # Methods
    def search_course(self):
        self.driver.refresh()
        time.sleep(5)
        self.iframe()
        time.sleep(5)
        self.click(self.list_of_course)
        self.input(self.search, test_date["date_course_name"])
        # self.input_search()
        # self.input_start_course()
        # self.input_stop_course()
        self.click(self.checkbox_off_filter)
        # self.click(self.checkbox_current_courses)
        # self.click(self.checkbox_past_courses)
        # self.click(self.checkbox_coming_courses)
        # self.click(self.checkbox_current_and_coming_courses)
        time.sleep(5)
        self.click(self.search_button)
        # self.get_name_of_course(self.name_of_course)
        time.sleep(2)
