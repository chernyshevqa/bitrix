import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base

"""Главная страница сайта"""


class New_course_page(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'

    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver

    # 05.10.2023

    test_date = {'date_course_name': 'test course', 'date_short_name_course': 'test',
                 'date_start_course': '2023-10-05', 'date_stop_course': '2023-10-31', 'date_course_version': '1',
                 'date_potok': '1',
                 'date_link_to_course': 'test.ru', 'date_discount_member_akpp': '10', 'date_discount_full_cource': '10',
                 'date_lead_plan': '200',
                 'date_start_RK': '2023-10-11', 'date_min_count_people': '10', 'date_activity_end_date': '2023-10-31',
                 'date_academic_hours': '200', 'date_all_tin': '10', 'date_all_intervision': '10',
                 'date_seminar_attendance': '80', 'date_attendance_ind_supervision': '100',
                 'date_progress_ind_supervision': '100', 'date_attendance_tin': '100', 'date_attendance_int': '100',
                 'date_group_supervision': '100',
                 'date_final_testing_seminar': '100', 'date_seminar_attendance_supervision': '100',
                 'date_attendance_ind_supervision_supervision': '100',
                 'date_progress_ind_supervision_supervision': '100', 'date_attendance_tin_supervision': '100',
                 'date_attendance_int_supervision': '100', 'date_group_supervision_supervision': '100',
                 'date_final_testing_seminar_supervision': '100', 'date_sert_group_supervision': '100',
                 'date_link_brif': 'test link', 'date_link_passport': 'test link pasport',
                 'date_promotion': '10',
                 'date_promotion_description': 'promotion_description',
                 'date_short_description_course': 'short_description_course',
                 'date_description_course': 'description_course', 'date_target_course': 'target_course',
                 'date_title_advantages_of_course': 'title_advantages_of_course',
                 'date_text_advantages_of_course': 'text_advantages_of_course',
                 'date_link_video_vizitka': 'link_video_vizitka',
                 'date_title_program_suitable': 'title_program_suitable',
                 'date_text_program_suitable': 'text_program_suitable', 'date_learning_results': 'learning_results',
                 'date_link_viodeofeedback': 'link_viodeofeedback', 'date_conditions_take_part': 'conditions_take_part',
                 'date_description_course_speakers': 'description_course_speakers', 'date_filed_of_FIO': 'filed_of_FIO',
                 'date_filed_of_feedback': 'filed_of_feedback', 'date_filed_of_cashback': 'filed_of_cashback'}

    dict_type_of_course = {'ТОП': 'ТОП', 'СТ': 'СТ', 'ПК': 'ПК', 'ДЭ': 'ДЭ', 'ДП': 'ДП', 'БК': 'БК'}
    name_of_course = "test course"
    link_to_course = "https://becbt.online/dashboard"
    difficulty = ["Начальный", "Продвинутый", "Экспертный"]
    yes_or_not = {'Да': 'Да', 'Нет': 'Нет'}
    dict_seller = {'АКППcbt': 'АКППcbt', 'АКППcbtunivercity': 'АКППcbtunivercity', 'АКПП cbttour': 'АКПП cbttour'
        , 'АКПП becbt': 'АКПП becbt', 'МИР КПТ': 'МИР КПТ'}
    dict_who_issues_certificates = {'Мир КПТ': 'Мир КПТ', 'АКПП': 'АКПП', 'Мир КПТ и АКПП': 'Мир КПТ и АКПП'}
    dict_department = {'ОКП': 'ОКП', 'НТ': 'НТ', 'НОМП': 'НОМП', 'КПК': 'КПК', }

    # Locators
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
    target_course = (By.XPATH, "//input[@id='target_course']")
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
    learning_results = (By.XPATH, "//input[@id='learning_outcomes']")
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
    button_add_course = (By.XPATH, "//button[@id='addCourse']")

    # Getters

    def iframe(self):
        return WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='app-frame']")))

    def get_performance_for_sertificat(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.performance_for_sertificat)))

    def get_edit_courses(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.edit_courses))

    def get_course_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.course_name))

    def get_search_courses(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.search_courses))

    def get_cancel_sending_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.cancel_sending_email))

    def get_short_name_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.short_name_course))

    def get_date_start_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.date_start_course))

    def get_date_stop_course(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.date_stop_course))

    def get_course_version(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.course_version))

    def get_potok(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.potok))

    def get_select_type_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.select_type_course))

    def get_difficulty_of_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.select_difficulty_of_course))

    def get_link_to_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.filed_link_to_course))

    def get_regionalCourse(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.select_regionalCourse))

    def get_seller(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.seller))

    def get_auto_send_document(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.auto_send_document))

    def get_discount_member_akpp(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.discount_member_akpp))

    def get_discount_full_cource(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.discount_full_cource))

    def get_lead_plan(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.lead_plan))

    def get_date_start_RK(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.date_start_RK))

    def get_min_count_people(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.min_count_people))

    def get_activity_end_date(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.activity_end_date))

    def get_sdo(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.sdo))

    def get_academic_hours(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.academic_hours))

    def get_who_issues_certificates(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.who_issues_certificates))

    def get_all_seminars(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.all_seminars))

    def get_all_tin(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.all_tin))

    def get_all_int(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.all_intervision))

    def get_sert_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.sert_course))

    def get_diplom_profy(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.diplom_profy))

    def get_udostoverenie_kurs(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.udostoverenie_kurs))

    def get_sert_all_seminar(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.sert_all_seminar))

    def get_sert_otd_seminar(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.sert_otd_seminar))

    def get_seminar_attendance(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.seminar_attendance))

    def get_attendance_ind_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.attendance_ind_supervision))

    def get_progress_ind_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.progress_ind_supervision))

    def get_attendance_tin(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.attendance_tin))

    def get_attendance_int(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.attendance_int))

    def get_group_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.group_supervision))

    def get_final_testing_seminar(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.final_testing_seminar))

    def get_itog_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.itog_supervision))

    def get_seminar_attendance_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.seminar_attendance_supervision))

    def get_attendance_ind_supervision_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.attendance_ind_supervision_supervision))

    def get_progress_ind_supervision_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.progress_ind_supervision_supervision))

    def get_attendance_tin_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.attendance_tin_supervision))

    def get_attendance_int_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.attendance_int_supervision))

    def get_group_supervision_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.group_supervision_supervision))

    def get_final_testing_seminar_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.final_testing_seminar_supervision))

    def get_sert_group_supervision(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.sert_group_supervision))

    def get_link_brif(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.link_brif))

    def get_link_passport(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.link_passport))

    def get_department(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.department))

    def get_promotion(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.promotion))

    def get_promotion_description(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.promotion_description))

    def get_short_description_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.short_description_course))

    def get_description_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.description_course))

    def get_target_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.target_course))

    def get_button_add_field_advantages_of_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.button_add_field_advantages_of_course))

    def get_title_advantages_of_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.title_advantages_of_course))

    def get_text_title_advantages_of_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.text_title_advantages_of_course))

    def get_delete_button_advantages_of_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.delete_button_advantages_of_course))

    def get_link_video_vizitka(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.link_video_vizitka))

    def get_button_add_field_program_suitable(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.button_add_field_program_suitable))

    def get_title_program_suitable(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.title_program_suitable))

    def get_text_program_suitable(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.text_program_suitable))

    def get_learning_results(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.learning_results))

    def get_button_add_field_videofeedback(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.button_add_field_videofeedback))

    def get_link_viodeofeedback(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.link_viodeofeedback))

    def get_conditions_take_part(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.conditions_take_part))

    def get_description_course_speakers(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.description_course_speakers))

    def get_button_add_field_feedback(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.button_add_field_feedback))

    def get_filed_of_FIO(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.filed_of_FIO))

    def get_filed_of_feedback(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.filed_of_feedback))

    def get_filed_of_cashback(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.filed_of_cashback))

    def get_button_add_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.button_add_course))

    # Methods
    def check_new_course(self):
        time.sleep(1)
        self.click(self.edit_courses), print("клик на кнопку изменить курс")
        self.assert_value_input(self.course_name, self.test_date['date_course_name'])
        self.assert_value_input(self.short_name_course, self.test_date['date_short_name_course'])
        self.assert_checkbox(self.cancel_sending_email)
        self.assert_value_input(self.date_start_course, self.test_date['date_start_course'])
        self.assert_value_input(self.date_stop_course, self.test_date['date_stop_course'])
        self.assert_value_input(self.course_version, self.test_date['date_course_version'])
        self.assert_value_input(self.potok, self.test_date['date_potok'])
        self.assert_value_select(self.select_type_course, self.dict_type_of_course['БК'])
        self.assert_value_select(self.select_difficulty_of_course, self.difficulty[2])
        self.assert_value_input(self.filed_link_to_course, self.test_date['date_link_to_course'])
        self.assert_value_select(self.select_regionalCourse, "Да")
        self.assert_value_select(self.seller, "akpp")
        self.assert_value_select(self.auto_send_document, "Да")
        self.assert_value_input(self.discount_member_akpp, self.test_date['date_discount_member_akpp'])
        self.assert_value_input(self.discount_full_cource, self.test_date['date_discount_full_cource'])
        self.assert_value_input(self.lead_plan, self.test_date['date_lead_plan'])
        self.assert_value_input(self.date_start_RK, self.test_date['date_start_RK'])
        self.assert_value_input(self.min_count_people, self.test_date['date_min_count_people'])
        self.assert_value_input(self.activity_end_date, self.test_date['date_activity_end_date'])
        # self.assert_value_input(self.sdo, self.test_date['date_sdo'])
        self.assert_value_input(self.academic_hours, self.test_date['date_academic_hours'])
        self.assert_value_select(self.who_issues_certificates, self.dict_who_issues_certificates['АКПП'])
        self.assert_value_select(self.all_seminars, self.yes_or_not['Да'])
        self.assert_value_input(self.all_tin, self.test_date['date_all_tin'])
        self.assert_value_input(self.all_intervision, self.test_date['date_all_intervision'])
        self.assert_value_select(self.sert_course, self.yes_or_not['Да'])
        self.assert_value_select(self.diplom_profy, self.yes_or_not['Да'])
        self.assert_value_select(self.udostoverenie_kurs, self.yes_or_not['Да'])
        self.assert_value_select(self.sert_all_seminar, self.yes_or_not['Да'])
        self.assert_value_select(self.sert_otd_seminar, self.yes_or_not['Да'])
        self.assert_value_input(self.seminar_attendance, self.test_date['date_seminar_attendance'])
        self.assert_value_input(self.attendance_ind_supervision, self.test_date['date_attendance_ind_supervision'])
        self.assert_value_input(self.progress_ind_supervision, self.test_date['date_progress_ind_supervision'])
        self.assert_value_input(self.attendance_tin, self.test_date['date_attendance_tin'])
        self.assert_value_input(self.attendance_int, self.test_date['date_attendance_int'])
        self.assert_value_input(self.group_supervision, self.test_date['date_group_supervision'])
        self.assert_value_input(self.final_testing_seminar, self.test_date['date_final_testing_seminar'])
        self.click(self.itog_supervision)
        self.assert_value_input(self.seminar_attendance_supervision,
                                self.test_date['date_seminar_attendance_supervision'])
        self.assert_value_input(self.attendance_ind_supervision_supervision,
                                self.test_date['date_attendance_ind_supervision_supervision'])
        self.assert_value_input(self.progress_ind_supervision_supervision,
                                self.test_date['date_progress_ind_supervision_supervision'])
        self.assert_value_input(self.attendance_tin_supervision, self.test_date['date_attendance_tin_supervision'])
        self.assert_value_input(self.attendance_int_supervision, self.test_date['date_attendance_int_supervision'])
        self.assert_value_input(self.group_supervision_supervision,
                                self.test_date['date_group_supervision_supervision'])
        self.assert_value_input(self.final_testing_seminar_supervision,
                                self.test_date['date_final_testing_seminar_supervision'])
        self.assert_value_input(self.sert_group_supervision, self.test_date['date_sert_group_supervision'])
        self.assert_value_input(self.link_brif, self.test_date['date_link_brif'])
        self.assert_value_input(self.link_passport, self.test_date['date_link_passport'])
        self.assert_value_select(self.department, self.dict_department['НТ'])
        self.assert_value_input(self.promotion, self.test_date['date_promotion'])
        self.assert_value_input(self.promotion_description, self.test_date['date_promotion_description'])
        self.assert_value_input(self.description_course, self.test_date['date_description_course'])
        self.assert_value_input(self.short_description_course, self.test_date['date_short_description_course'])
        self.assert_value_input(self.target_course, self.test_date['date_target_course'])
        self.assert_value_input(self.title_advantages_of_course, self.test_date['date_title_advantages_of_course'])
        self.assert_value_input(self.text_advantages_of_course, self.test_date['date_text_advantages_of_course'])
        self.assert_value_input(self.link_video_vizitka, self.test_date['date_link_video_vizitka'])
        self.assert_value_input(self.title_program_suitable, self.test_date['date_title_program_suitable'])
        self.assert_value_input(self.text_program_suitable, self.test_date['date_text_program_suitable'])
        self.assert_value_input(self.learning_results, self.test_date['date_learning_results'])
        self.assert_value_input(self.link_viodeofeedback, self.test_date['date_link_viodeofeedback'])
        self.assert_value_input(self.conditions_take_part, self.test_date['date_conditions_take_part'])
        self.assert_value_input(self.description_course_speakers, self.test_date['date_description_course_speakers'])
        self.assert_value_input(self.filed_of_FIO, self.test_date['date_filed_of_FIO'])
        # self.assert_value_input(self.filed_of_feedback, self.test_date['date_filed_of_feedback'])