import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pajes.main_page import Main_page
from pajes.login_page import Login_page
from pajes.page_create_courses import Create_new_course_page
from pajes.search_course_page import Search_course
from pajes.page_course_assert import New_course_page



def test_search_course():

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test 1")

    login = Login_page(driver)
    login.autorization()

    sc = Search_course(driver)
    sc.search_course()

    check_course = New_course_page(driver)
    check_course.check_new_course()


    print("finish test 1")
    driver.quit()