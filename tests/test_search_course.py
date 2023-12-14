from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pajes.login_page import Login_page
from pajes.search_course_page import Search_course


# from pajes.add_other_practice_page import Add_practise


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

    print("finish test 1")
    driver.quit()