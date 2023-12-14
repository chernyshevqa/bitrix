import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pajes.login_page import Login_page
from pajes.add_practice_seminar_page import Add_practise
from pajes.create_page_short import Create_new_course_page_short
from pajes.page_course_assert import assert_page
from pajes.delete_course_page import Delete_course

"""Тест для создания практик в курсе проверка практик"""
def test_add_practices():
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

    create_course = Create_new_course_page_short(driver)
    create_course.create_new_course()

    adpr = Add_practise(driver)
    adpr.practise_add()

    ass = assert_page(driver)
    ass.check_new_course()

    delete_course = Delete_course(driver)
    delete_course.test_delete_course()

    print("finish test 1")
    driver.quit()
