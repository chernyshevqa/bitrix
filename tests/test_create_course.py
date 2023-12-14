from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pajes.login_page import Login_page
from pajes.create_page_short import Create_new_course_page_short
from pajes.search_course_page import Search_course
from pajes.page_course_assert import assert_page
from pajes.delete_course_page import Delete_course

"""Создание курса"""
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

    print("Create")
    cc = Create_new_course_page_short(driver)
    cc.create_new_course()

    print("Search")
    sc = Search_course(driver)
    sc.search_course()

    print("assert")
    ass = assert_page(driver)
    ass.check_new_course()

    print("delete")
    delete_course = Delete_course(driver)
    delete_course.test_delete_course()


    print("finish test 1")
