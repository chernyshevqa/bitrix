import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pajes.main_page import Main_page
from pajes.login_page import Login_page
from pajes.search_course_page import Search_course
from pajes.page_course_assert import assert_page
from pajes.create_deal import Create_deal




def test_check_new_course():

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

    create = Create_deal(driver)
    create.create_deals()

    print("finish test 1")
    driver.quit()