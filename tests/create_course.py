import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pajes.main_page import Main_page
from pajes.login_page import Login_page
from pajes.create_page_short import Create_new_course_page_short

def test_create_new_course():

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

    cc = Create_new_course_page_short(driver)
    cc.create_new_course()




    print("finish test 1")
    driver.quit()