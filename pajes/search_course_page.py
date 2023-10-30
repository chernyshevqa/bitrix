# import time
import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


"""Главная страница сайта"""
class Search_course(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'
    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver


    name_of_course = "test course"
    # Locators
    # course = "//a[text() ='Курсы']"

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



    # Getters

    def iframe(self):
        return WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='app-frame']")))

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.search))

    def get_start_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.start_course)))

    def get_stop_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.stop_course)))

    def get_course_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.course_name)))

    #actions
    def input_search(self):
        self.get_search().send_keys("test course")
        print("ввод курса в поиске")

    def input_start_course(self):
        self.get_start_course().send_keys("18.10.2023")
        print("ввод даты начала курса")

    def input_stop_course(self):
        self.get_stop_course().send_keys("31.10.2023")
        print("ввод даты окончания курса")

    def click_course_name(self):
        self.get_course_name().click()
        print("клик курс")






    # Methods
    def search_course(self):
        self.get_current_url()
        time.sleep(7)
        self.iframe()
        time.sleep(3)
        self.input(self.search, "test course")
        # self.input_search()
        # self.input_start_course()
        # self.input_stop_course()
        # self.click(self.checkbox_off_filter)
        # self.click(self.checkbox_current_courses)
        # self.click(self.checkbox_past_courses)
        # self.click(self.checkbox_coming_courses)
        # self.click(self.checkbox_current_and_coming_courses)
        time.sleep(1)
        self.click(self.search_button)
        # self.click_search_button()
        time.sleep(2)
        self.click_course_name()
        time.sleep(2)
        # assert self.get_text(" test course"), "Текст 'test course' не найден на странице"