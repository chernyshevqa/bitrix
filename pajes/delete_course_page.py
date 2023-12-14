# import time
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data.data_test import *
from base.base_class import Base


"""Главная страница сайта"""
class Delete_course(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'
    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver


    name_of_course = f"{course_name}"
    # Locators
    # course = "//a[text() ='Курсы']"
    course_name = (By.XPATH, f"//span[@id='course_name'][text()=' {name_of_course}']")
    edit_courses = (By.XPATH, "//button[@class='button_ok openUpdateCourse']")
    button_delete_course = (By.XPATH, "//button[@id='delCourse']")
    search = (By.XPATH, "//input[@id='name_сourse_search']")
    search_button = (By.XPATH, "//button[@class='button_ok сourse_search']")
    # Getters

    def iframe(self):
        return WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='app-frame']")))

    # Methods
    def test_delete_course(self):
        self.driver.refresh()
        self.iframe()
        time.sleep(10)
        self.input(self.search, test_date["date_course_name"])
        self.click(self.search_button)
        self.click(self.course_name)
        self.click(self.edit_courses)
        self.click(self.button_delete_course)
        self.switch_to_alert()


