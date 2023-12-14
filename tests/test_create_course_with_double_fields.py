from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pajes.login_page import Login_page
from pajes.create_page_with_double_fields import Create_new_course_lending_x2
from pajes.page_course_assert import assert_page
from pajes.delete_course_page import Delete_course
from pajes.add_practice_seminar_page import Add_practise

"""Создание курса с дублированными полями"""
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

    cc = Create_new_course_lending_x2(driver)
    cc.create_new_course()

    adpr = Add_practise(driver)
    adpr.practise_add()

    ass = assert_page(driver)
    ass.check_new_course()

    delete_course = Delete_course(driver)
    delete_course.test_delete_course()

    driver.quit()
    print("finish test 1")
