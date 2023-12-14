import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from test_data.data_test import *
"""Главная страница сайта"""


class assert_page(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'

    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver

    # Locators
    name_of_course = test_date['date_course_name']
    course_name_after_search = (By.XPATH, f"//span[@id='course_name'][text()=' {name_of_course}']")
    button_open_sertification = (By.XPATH, "//*[contains(text(), 'Сертификация и успеваемость:')]")
    performance_for_sertificat = "//*[contains(text(), 'Необходимая успеваемость для сертификата:')]"
    # edit_course = "//*[contains(text(), 'Изменить курс')]"
    edit_courses = (By.XPATH, "//button[@class='button_ok openUpdateCourse']")
    course_name = (By.XPATH, "//input[@id='nameCourse']")
    search_courses = (By.XPATH, "//input[@id='name_сourse_search']")
    cancel_sending_email = (By.XPATH, "//input[@id='сancelSendingEmails']")
    short_name_course = (By.XPATH, "//input[@id='shortNameCourse']")
    date_start_course = (By.XPATH, "//input[@id='dateStartCourse']")
    date_stop_course = (By.XPATH, "//input[@id='dateStopCourse']")
    course_version = (By.XPATH, "//input[@id='verCourse']")
    potok = (By.XPATH, "//input[@id='parentStreamCourse']")
    select_type_course = (By.XPATH, "//select[@id='type_course_package']")
    select_difficulty_of_course = (By.XPATH, "//select[@id='difficulty']")
    filed_link_to_course = (By.XPATH, "//input[@id='linkCourse']")
    select_regionalCourse = (By.XPATH, "//select[@id='regionalCourse']")
    seller = (By.XPATH, "//select[@id='seller']")
    take_part = (By.XPATH, "//select[@id='pointEvent']")
    auto_send_document = (By.XPATH, "//select[@id='auto_send_document']")
    discount_member_akpp = (By.XPATH, "//input[@id='discountMemberAkpp']")
    discount_full_cource = (By.XPATH, "//input[@id='discountFullCource']")
    lead_plan = (By.XPATH, "//input[@id='leadPlan']")
    date_start_RK = (By.XPATH, "//input[@id='dateStartRK']")
    min_count_people = (By.XPATH, "//input[@id='mincountpeople']")
    activity_end_date = (By.XPATH, "//input[@id='activity_end_date']")
    sdo = (By.XPATH, "//input[@id='sdo']")
    academic_hours = (By.XPATH, "//input[@id='academichours']")
    who_issues_certificates = (By.XPATH, "//select[@id='who_issues_certificates']")
    all_seminars = (By.XPATH, "//select[@id='all_seminars']")
    all_tin = (By.XPATH, "//input[@id='all_tin']")
    all_intervision = (By.XPATH, "//input[@id='all_int']")
    sert_course = (By.XPATH, "//select[@id='sert_course']")
    diplom_profy = (By.XPATH, "//select[@id='diplom_profy']")
    udostoverenie_kurs = (By.XPATH, "//select[@id='udost_kurs']")
    sert_all_seminar = (By.XPATH, "//select[@id='sert_all_seminar']")
    sert_otd_seminar = (By.XPATH, "//select[@id='sert_otd_seminar']")
    seminar_attendance = (By.XPATH, "//input[@id='seminar_attendance']")
    attendance_ind_supervision = (By.XPATH, "//input[@id='attendance_ind_supervision']")
    progress_ind_supervision = (By.XPATH, "//input[@id='progress_ind_supervision']")
    attendance_tin = (By.XPATH, "//input[@id='attendance_tin']")
    attendance_int = (By.XPATH, "//input[@id='attendance_int']")
    group_supervision = (By.XPATH, "//input[@id='group_supervizii']")
    final_testing_seminar = (By.XPATH, "//input[@id='final_testing_seminar']")

    """Необходимая успеваемость для допуска к итоговой супервизии"""
    itog_supervision = (
        By.XPATH, "//*[contains(text(), 'Необходимая успеваемость для допуска к итоговой супервизии:')]")
    seminar_attendance_supervision = (By.XPATH, "//input[@id='seminar_attendance_supervizii']")
    attendance_ind_supervision_supervision = (By.XPATH, "//input[@id='attendance_ind_supervision_supervizii']")
    progress_ind_supervision_supervision = (By.XPATH, "//input[@id='progress_ind_supervision_supervizii']")
    attendance_tin_supervision = (By.XPATH, "//input[@id='attendance_tin_supervizii']")
    attendance_int_supervision = (By.XPATH, "//input[@id='attendance_int_supervizii']")
    group_supervision_supervision = (By.XPATH, "//input[@id='group_supervizii_supervizii']")
    final_testing_seminar_supervision = (By.XPATH, "//input[@id='final_testing_seminar_supervizii']")

    """Доп информация для формирования страниц"""
    sert_group_supervision = (By.XPATH, "//input[@id='sert_group_supervizii']")
    link_brif = (By.XPATH, "//input[@id='link_brif']")
    link_passport = (By.XPATH, "//input[@id='link_passport']")
    department = (By.XPATH, "//select[@id='department']")
    promotion = (By.XPATH, "//input[@id='promotion']")
    promotion_description = (By.XPATH, "//textarea[@id='promotion_str']")
    description_course = (By.XPATH, "//textarea[@id='description_course']")
    short_description_course = (By.XPATH, "//textarea[@id='sokr_description_course']")
    button_target_course = (By.XPATH,
                            '//button[@onclick="createFieldTargetCourse(document.getElementsByClassName(\'program-container-target_course\')[0])"]')
    target_course = (By.XPATH,
                     "//div[@class='program-item program-item--adv program-item--adv-target_course']//input[@class='main_select' and @placeholder='Заголовок']")
    button_add_field_advantages_of_course = (By.XPATH,
                                             '//button[@onclick="createField(document.getElementsByClassName(\'program-container-benefits_program\')[0])"]')
    title_advantages_of_course = (By.XPATH,
                                  "//div[@class='program-item program-item--adv program-item--adv-benefits_program']//input[@class='main_select' and @placeholder='Заголовок']")
    text_advantages_of_course = (By.XPATH,
                                       "//div[@class='program-item program-item--adv program-item--adv-benefits_program']//textarea[@placeholder='Текст']")
    delete_button_advantages_of_course = (By.XPATH,
                                          "//div[@class='program-item program-item--adv program-item--adv-benefits_program']//i[@class='fa fa-trash']")
    link_video_vizitka = (By.XPATH, "//input[@id='link_video_vizit']")
    button_add_field_program_suitable = (By.XPATH,
                                         '//button[@onclick="createFieldProgramSuitable(document.getElementsByClassName(\'program-container-program_suitable\')[0])"]')
    title_program_suitable = (By.XPATH,
                              "//div[@class='program-item program-item--adv program-item--adv-program_suitable']//input[@placeholder='Заголовок']")
    text_program_suitable = (By.XPATH,
                             "//div[@class='program-item program-item--adv program-item--adv-program_suitable']//textarea[@placeholder='Текст']")
    button_add_learning_results = (By.XPATH, "//button[@onclick='renderFieldLearningOutcomes()']")
    learning_results_title = (By.XPATH, "//div[@id='learning_outcomes']//input[@placeholder='Заголовок']")
    learning_results_text = (By.XPATH, "//div[@id='learning_outcomes']//textarea[@placeholder='Текст']")
    button_add_field_videofeedback = (By.XPATH,
                                      '//button[@onclick="createFieldVideoReviews(document.getElementsByClassName(\'program-container-video_reviews\')[0])"]')
    link_viodeofeedback = (By.XPATH,
                           "//div[@class='program-item program-item--adv program-item--adv-video_reviews']//input[@placeholder='Ссылка']")
    conditions_take_part = (By.XPATH, "//input[@id='terms_participation']")
    description_course_speakers = (By.XPATH, "//textarea[@id='description_course_speakers']")
    button_add_field_feedback = (By.XPATH, "//button[@onclick='renderFieldReview()']")
    filed_of_FIO = (By.XPATH, "//input[@placeholder='ФИО']")
    filed_of_feedback = (By.XPATH, "//textarea[@placeholder='Отзыв2']")
    filed_of_cashback = (By.XPATH, "//input[@id='kaschback']")
    lending = (By.XPATH, "//select[@id='generate_lending']")
    autopay = (By.XPATH, "//select[@id='autopay']")
    description_course_programm = (By.XPATH, "//input[@id='description_program']")
    prise_course = (By.XPATH, "//input[@id='price_course']")
    info_sertification = (By.XPATH, "//textarea[@id='info_sert']")
    button_add_field_FAQ = By.XPATH, '//button[@onclick="createFieldFaq(document.getElementsByClassName(\'program-container-faq\')[0])"]'
    FAQ_title = (
    By.XPATH, "//div[@class='program-item program-item--adv program-item--adv-faq']//input[@placeholder='Заголовок']")
    FAQ_text = (
    By.XPATH, "//div[@class='program-item program-item--adv program-item--adv-faq']//textarea[@placeholder='Текст']")
    button_add_course = (By.XPATH, "//button[@id='addCourse']")

    # Getters

    def iframe(self):
        return WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='app-frame']")))

    # Methods
    def check_new_course(self):
        with allure.step("проверка всех полей"):
            time.sleep(1)
            self.click(self.course_name_after_search)
            self.click(self.edit_courses)
            self.assert_value_input(self.course_name, test_date['date_course_name'])
            self.assert_value_input(self.short_name_course, test_date['date_short_name_course'])
            self.assert_checkbox(self.cancel_sending_email)
            self.assert_value_input(self.date_start_course, "2023-11-15")
            self.assert_value_input(self.date_stop_course, "2023-11-30")
            self.assert_value_input(self.course_version, test_date['date_course_version'])
            self.assert_value_input(self.potok, test_date['date_potok'])
            self.assert_value_select(self.select_type_course, dict_type_of_course['БК'])
            self.assert_value_select(self.select_difficulty_of_course, difficulty[2])
            self.assert_value_input(self.filed_link_to_course, test_date['date_link_to_course'])
            self.assert_value_select(self.select_regionalCourse, "Да")
            self.assert_value_select(self.seller, "akpp")
            self.assert_value_select(self.auto_send_document, "Да")
            self.assert_value_select(self.take_part, "3")
            self.assert_value_input(self.discount_member_akpp, test_date['date_discount_member_akpp'])
            self.assert_value_input(self.discount_full_cource, test_date['date_discount_full_cource'])
            self.assert_value_input(self.lead_plan, test_date['date_lead_plan'])
            self.assert_value_input(self.date_start_RK, "2023-10-11")
            self.assert_value_input(self.min_count_people, test_date['date_min_count_people'])
            self.assert_value_input(self.activity_end_date, "2023-10-31")
            # self.assert_value_input(self.sdo, self.test_date['date_sdo'])
            self.assert_value_input(self.academic_hours, test_date['date_academic_hours'])
            self.assert_value_select(self.department, dict_department['НТ'])
            self.assert_value_input(self.link_brif, test_date['date_link_brif'])
            self.assert_value_input(self.link_passport, test_date['date_link_passport'])
            """Сертификаты"""
            self.click(self.button_open_sertification)
            self.assert_value_select(self.who_issues_certificates, dict_who_issues_certificates['АКПП'])
            self.assert_value_select(self.all_seminars, yes_or_not['Да'])
            self.assert_value_input(self.all_tin, test_date['date_all_tin'])
            self.assert_value_input(self.all_intervision, test_date['date_all_intervision'])
            self.assert_value_select(self.sert_course, yes_or_not['Да'])
            self.assert_value_select(self.diplom_profy, yes_or_not['Да'])
            self.assert_value_select(self.udostoverenie_kurs, yes_or_not['Да'])
            self.assert_value_select(self.sert_all_seminar, yes_or_not['Да'])
            self.assert_value_select(self.sert_otd_seminar, yes_or_not['Да'])
            """Лендинг"""
            # self.assert_value_input(self.promotion, test_date['date_promotion'])
            # self.assert_value_input(self.promotion_description, test_date['date_promotion_description'])
            # self.assert_value_input(self.short_description_course, test_date['date_short_description_course'])
            # self.assert_value_input(self.description_course, test_date['date_description_course'])
            # self.assert_value_input(self.target_course, test_date['date_target_course'])
            # self.assert_value_input(self.description_course_speakers, test_date['date_description_course_speakers'])
            # self.assert_value_input(self.filed_of_FIO, test_date['date_filed_of_FIO'])
            # self.assert_value_input(self.filed_of_feedback, test_date['date_filed_of_feedback'])
            # self.assert_value_select(self.autopay, yes_or_not['Да'])
            # self.assert_value_input(self.title_advantages_of_course, test_date['date_title_advantages_of_course'])
            # self.assert_value_input(self.text_advantages_of_course, test_date['date_text_advantages_of_course'])
            # self.assert_value_input(self.link_video_vizitka, test_date['date_link_video_vizitka'])
            # self.assert_value_input(self.title_program_suitable, test_date['date_title_program_suitable'])
            # self.assert_value_input(self.text_program_suitable, test_date['date_text_program_suitable'])
            # self.assert_value_input(self.learning_results_title, test_date['date_learning_results'])
            # self.assert_value_input(self.learning_results_text, test_date['date_learning_results'])
            # self.assert_value_input(self.link_viodeofeedback, test_date['date_link_viodeofeedback'])
            # self.assert_value_input(self.conditions_take_part, test_date['date_conditions_take_part'])
            # self.assert_value_input(self.description_course_programm, test_date['date_description_course_programm'])
            # self.assert_value_input(self.prise_course, test_date['date_prise_course'])
            # self.assert_value_input(self.info_sertification, test_date['date_info_sertification'])
            # self.assert_value_input(self.FAQ_title, test_date['date_FAQ_title'])
            # self.assert_value_input(self.FAQ_text, test_date['date_FAQ_text'])
            # self.assert_value_select(self.lending, yes_or_not['Да'])
            # self.assert_value_input(self.filed_of_cashback, test_date['date_filed_of_cashback'])

            """данные для получения сертификатов"""
            self.assert_value_input(self.seminar_attendance, test_date['date_seminar_attendance'])
            self.assert_value_input(self.attendance_ind_supervision, test_date['date_attendance_ind_supervision'])
            self.assert_value_input(self.progress_ind_supervision, test_date['date_progress_ind_supervision'])
            self.assert_value_input(self.attendance_tin, test_date['date_attendance_tin'])
            self.assert_value_input(self.attendance_int, test_date['date_attendance_int'])
            self.assert_value_input(self.group_supervision, test_date['date_group_supervision'])
            self.assert_value_input(self.final_testing_seminar, test_date['date_final_testing_seminar'])
            self.assert_value_input(self.seminar_attendance_supervision, test_date['date_seminar_attendance_supervision'])
            self.assert_value_input(self.attendance_ind_supervision_supervision,
                                    test_date['date_attendance_ind_supervision_supervision'])
            self.assert_value_input(self.progress_ind_supervision_supervision,
                                    test_date['date_progress_ind_supervision_supervision'])
            self.assert_value_input(self.attendance_tin_supervision, test_date['date_attendance_tin_supervision'])
            self.assert_value_input(self.attendance_int_supervision, test_date['date_attendance_int_supervision'])
            self.assert_value_input(self.group_supervision_supervision,
                                    test_date['date_group_supervision_supervision'])
            self.assert_value_input(self.final_testing_seminar_supervision,
                                    test_date['date_final_testing_seminar_supervision'])
            self.assert_value_input(self.sert_group_supervision, test_date['date_sert_group_supervision'])


