import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base

"""Главная страница сайта"""


class Create_new_course_page_1(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'

    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver

    #needed date
    dict_type_of_course = {'ТОП': 'ТОП', 'СТ': 'СТ', 'ПК': 'ПК', 'ДЭ': 'ДЭ', 'ДП': 'ДП', 'БК': 'БК'}
    name_of_course = "test course"
    link_to_course = "https://becbt.online/dashboard"
    difficulty = ["Начальный", "Продвинутый", "Экспертный"]
    yes_or_not = {'Да': 'Да', 'Нет': 'Нет'}
    dict_seller = {'АКППcbt': 'АКППcbt', 'АКППcbtunivercity': 'АКППcbtunivercity', 'АКПП cbttour': 'АКПП cbttour'
        , 'АКПП becbt': 'АКПП becbt', 'МИР КПТ': 'МИР КПТ'}
    dict_who_issues_certificates = {'Мир КПТ': 'Мир КПТ', 'АКПП': 'АКПП', 'Мир КПТ и АКПП': 'Мир КПТ и АКПП'}
    dict_department = {'ОКП': 'ОКП', 'НТ': 'НТ', 'НОМП': 'НОМП', 'КПК': 'КПК', }

    test_date = {'date_course_name': ' test course', 'date_short_name_course': 'test',
                 'date_start_course': '05.10.2023', 'date_stop_course': '31.10.2023', 'date_course_version': '1',
                 'date_potok': '1',
                 'date_link_to_course': 'test.link', 'date_discount_member_akpp': '10', 'date_discount_full_cource': '10',
                 'date_lead_plan': '200',
                 'date_start_RK': '11.10.2023', 'date_min_count_people': '1', 'date_activity_end_date': '31.10.2023',
                 'date_academic_hours': '20', 'date_all_tin': '10', 'date_all_intervision': '10',
                 'date_seminar_attendance': '80', 'date_attendance_ind_supervision': '100',
                 'date_progress_ind_supervision': '100', 'date_attendance_tin': '100', 'date_attendance_int': '100',
                 'date_group_supervision': '100',
                 'date_final_testing_seminar': '100', 'date_seminar_attendance_supervision': '100',
                 'date_attendance_ind_supervision_supervision': '100',
                 'date_progress_ind_supervision_supervision': '100', 'date_attendance_tin_supervision': '100',
                 'date_attendance_int_supervision': '100', 'date_group_supervision_supervision': '100',
                 'date_final_testing_seminar_supervision': '100', 'date_sert_group_supervision': '100',
                 'date_link_brif': 'test link', 'date_link_passport': 'test link pasport',
                 'date_promotion': 'promotion',
                 'date_promotion_description': 'promotion_description',
                 'date_short_description_course': 'short_description_course',
                 'date_description_course': 'description_course', 'date_target_course': 'target_course',
                 'date_title_advantages_of_course': 'title_advantages_of_course',
                 'date_text_title_advantages_of_course': 'text_title_advantages_of_course',
                 'date_link_video_vizitka': 'link_video_vizitka',
                 'date_title_program_suitable': 'title_program_suitable',
                 'date_text_program_suitable': 'text_program_suitable', 'date_learning_results': 'learning_results',
                 'date_link_viodeofeedback': 'link_viodeofeedback', 'date_conditions_take_part': 'conditions_take_part',
                 'date_description_course_speakers': 'description_course_speakers', 'date_filed_of_FIO': 'filed_of_FIO',
                 'date_filed_of_feedback': 'filed_of_feedback', 'date_filed_of_cashback': 'filed_of_cashback'}


    # Locators
    performance_for_sertificat = "//*[contains(text(), 'Необходимая успеваемость для сертификата:')]"
    add_courses = "//button[@class='button_ok openAddCourse']"
    course_name = "//input[@id='nameCourse']"
    search_courses = "//input[@id='name_сourse_search']"
    cancel_sending_email = "//input[@id='сancelSendingEmails']"
    short_name_course = "//input[@id='shortNameCourse']"
    date_start_course = "//input[@id='dateStartCourse']"
    date_stop_course = "//input[@id='dateStopCourse']"
    course_version = "//input[@id='verCourse']"
    potok = "//input[@id='parentStreamCourse']"
    select_type_course = "//select[@id='type_course_package']"
    select_difficulty_of_course = "//select[@id='difficulty']"
    filed_link_to_course = "//input[@id='linkCourse']"
    select_regionalCourse = "//select[@id='regionalCourse']"
    seller = "//select[@id='seller']"
    auto_send_document = "//select[@id='auto_send_document']"
    discount_member_akpp = (By.XPATH, "//input[@id='discountMemberAkpp']")
    discount_full_cource = (By.XPATH,  "//input[@id='discountFullCource']")
    lead_plan = "//input[@id='leadPlan']"
    date_start_RK = "//input[@id='dateStartRK']"
    min_count_people = "//input[@id='mincountpeople']"
    activity_end_date = "//input[@id='activity_end_date']"
    sdo = "//input[@id='sdo']"
    academic_hours = "//input[@id='academichours']"
    who_issues_certificates = "//select[@id='who_issues_certificates']"
    all_seminars = "//select[@id='all_seminars']"
    all_tin = "//input[@id='all_tin']"
    all_intervision = "//input[@id='all_int']"
    sert_course = "//select[@id='sert_course']"
    diplom_profy = "//select[@id='diplom_profy']"
    udostoverenie_kurs = "//select[@id='udost_kurs']"
    sert_all_seminar = "//select[@id='sert_all_seminar']"
    sert_otd_seminar = "//select[@id='sert_otd_seminar']"
    seminar_attendance = (By.XPATH, "//input[@id='seminar_attendance']")
    attendance_ind_supervision = (By.XPATH, "//input[@id='attendance_ind_supervision']")
    progress_ind_supervision = (By.XPATH, "//input[@id='progress_ind_supervision']")
    attendance_tin = (By.XPATH, "//input[@id='attendance_tin']")
    attendance_int = (By.XPATH, "//input[@id='attendance_int']")
    group_supervision = (By.XPATH, "//input[@id='group_supervizii']")
    final_testing_seminar = (By.XPATH, "//input[@id='final_testing_seminar']")
    seminar_attendance_supervision = (By.XPATH, "//input[@id='seminar_attendance_supervizii']")

    """Необходимая успеваемость для допуска к итоговой супервизии"""
    itog_supervision = "//*[contains(text(), 'Необходимая успеваемость для допуска к итоговой супервизии:')]"
    attendance_ind_supervision_supervision = (By.XPATH, "//input[@id='attendance_ind_supervision_supervizii']")
    progress_ind_supervision_supervision = (By.XPATH, "//input[@id='progress_ind_supervision_supervizii']")
    attendance_tin_supervision = (By.XPATH, "//input[@id='attendance_tin_supervizii']")
    attendance_int_supervision = (By.XPATH, "//input[@id='attendance_int_supervizii']")
    group_supervision_supervision = (By.XPATH, "//input[@id='group_supervizii_supervizii']")
    final_testing_seminar_supervision = (By.XPATH, "//input[@id='final_testing_seminar_supervizii']")

    """Доп информация для формирования страниц"""
    sert_group_supervision = (By.XPATH,  "//input[@id='sert_group_supervizii']")
    link_brif = "//input[@id='link_brif']"
    link_passport = "//input[@id='link_passport']"
    department = "//select[@id='department']"
    promotion = (By.XPATH,   "//input[@id='promotion']")
    promotion_description = "//textarea[@id='promotion_str']"
    description_course = "//textarea[@id='description_course']"
    short_description_course = "//textarea[@id='sokr_description_course']"
    target_course = "//input[@id='target_course']"
    button_add_field_advantages_of_course = '//button[@onclick="createField(document.getElementsByClassName(\'program-container-benefits_program\')[0])"]'
    title_advantages_of_course = "//div[@class='program-item program-item--adv program-item--adv-benefits_program']//input[@class='main_select' and @placeholder='Заголовок']"
    text_title_advantages_of_course = "//div[@class='program-item program-item--adv program-item--adv-benefits_program']//textarea[@placeholder='Текст']"
    delete_button_advantages_of_course = "//div[@class='program-item program-item--adv program-item--adv-benefits_program']//i[@class='fa fa-trash']"
    link_video_vizitka = "//input[@id='link_video_vizit']"
    button_add_field_program_suitable = '//button[@onclick="createFieldProgramSuitable(document.getElementsByClassName(\'program-container-program_suitable\')[0])"]'
    title_program_suitable = "//div[@class='program-item program-item--adv program-item--adv-program_suitable']//input[@placeholder='Заголовок']"
    text_program_suitable = "//div[@class='program-item program-item--adv program-item--adv-program_suitable']//textarea[@placeholder='Текст']"
    learning_results = "//input[@id='learning_outcomes']"
    button_add_field_videofeedback = '//button[@onclick="createFieldVideoReviews(document.getElementsByClassName(\'program-container-video_reviews\')[0])"]'
    link_viodeofeedback = "//div[@class='program-item program-item--adv program-item--adv-video_reviews']//input[@placeholder='Ссылка']"
    conditions_take_part = "//input[@id='terms_participation']"
    description_course_speakers = "//textarea[@id='description_course_speakers']"
    button_add_field_feedback = "//button[@onclick='renderFieldReview()']"
    filed_of_FIO = "//input[@placeholder='ФИО']"
    filed_of_feedback = "//textarea[@placeholder='Отзыв2']"
    filed_of_cashback = (By.XPATH, "//input[@id='kaschback']")
    button_add_course = "//button[@id='addCourse']"
    # Getters

    def iframe(self):
        return WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='app-frame']")))

    def get_performance_for_sertificat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.performance_for_sertificat)))

    def get_add_courses(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_courses)))

    def get_course_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.course_name)))

    def get_search_courses(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.search_courses)))

    def get_cancel_sending_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.cancel_sending_email)))

    def get_short_name_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.short_name_course)))

    def get_date_start_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.date_start_course)))

    def get_date_stop_course(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.date_stop_course)))

    def get_course_version(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.course_version)))

    def get_potok(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.potok)))

    def get_select_type_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.select_type_course)))

    def get_difficulty_of_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.select_difficulty_of_course)))

    def get_link_to_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.filed_link_to_course)))

    def get_regionalCourse(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.select_regionalCourse)))

    def get_seller(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.seller)))

    def get_auto_send_document(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.auto_send_document)))

    def get_discount_member_akpp(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.discount_member_akpp))

    def get_discount_full_cource(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.discount_full_cource))

    def get_lead_plan(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.lead_plan)))

    def get_date_start_RK(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.date_start_RK)))

    def get_min_count_people(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.min_count_people)))

    def get_activity_end_date(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.activity_end_date)))

    def get_sdo(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.sdo)))

    def get_academic_hours(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.academic_hours)))

    def get_who_issues_certificates(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.who_issues_certificates)))

    def get_all_seminars(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.all_seminars)))

    def get_all_tin(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.all_tin)))

    def get_all_int(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.all_intervision)))

    def get_sert_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.sert_course)))

    def get_diplom_profy(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.diplom_profy)))

    def get_udostoverenie_kurs(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.udostoverenie_kurs)))

    def get_sert_all_seminar(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.sert_all_seminar)))

    def get_sert_otd_seminar(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.sert_otd_seminar)))

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
            EC.element_to_be_clickable((By.XPATH, self.itog_supervision)))

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
            EC.visibility_of_element_located((By.XPATH, self.link_brif)))

    def get_link_passport(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.link_passport)))

    def get_department(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.department)))

    def get_promotion(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.promotion))

    def get_promotion_description(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.promotion_description)))

    def get_short_description_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.short_description_course)))

    def get_description_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.description_course)))

    def get_target_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.target_course)))

    def get_button_add_field_advantages_of_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.button_add_field_advantages_of_course)))

    def get_title_advantages_of_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.title_advantages_of_course)))

    def get_text_title_advantages_of_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.text_title_advantages_of_course)))

    def get_delete_button_advantages_of_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.delete_button_advantages_of_course)))

    def get_link_video_vizitka(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.link_video_vizitka)))

    def get_button_add_field_program_suitable(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.button_add_field_program_suitable)))

    def get_title_program_suitable(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.title_program_suitable)))

    def get_text_program_suitable(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.text_program_suitable)))

    def get_learning_results(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.learning_results)))

    def get_button_add_field_videofeedback(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.button_add_field_videofeedback)))

    def get_link_viodeofeedback(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.link_viodeofeedback)))

    def get_conditions_take_part(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.conditions_take_part)))

    def get_description_course_speakers(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.description_course_speakers)))

    def get_button_add_field_feedback(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.button_add_field_feedback)))

    def get_filed_of_FIO(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.filed_of_FIO)))

    def get_filed_of_feedback(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.filed_of_feedback)))

    def get_filed_of_cashback(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.filed_of_cashback))

    def get_button_add_course(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.button_add_course)))


    # action
    def click_add_courses(self):
        self.get_add_courses().click()
        print("клик на добавить курс")

    def input_course_name(self):
        self.get_course_name().send_keys(self.name_of_course)
        print("ввод названия курса")

    def click_cancel_sending_email(self):
        self.get_cancel_sending_email().click()
        print("клик на чекбокс отмены отправки сообщения")

    def input_short_name_course(self):
        self.get_short_name_course().send_keys(self.name_of_course)
        print("ввод короткого названия курса")

    def input_date_start_course(self):
        self.get_date_start_course().send_keys("05.10.2023")
        print("ввод даты начала курса")

    def input_date_stop_course(self):
        self.get_date_stop_course().send_keys("31.10.2023")
        print("ввод даты окончания курса")

    def input_course_version(self):
        self.get_course_version().send_keys("1")
        print("ввод версии курса")

    def input_potok(self):
        self.get_potok().send_keys("1")
        print("ввод потока курса")

    def click_select_type_course(self):
        self.get_select_type_course().click()
        print("клик на выпадающий список типов курсов")

    def click_select_difficulty_of_course(self):
        self.get_difficulty_of_course().click()
        print("клик на выпадающий список сложности курсов")

    def input_link_to_course(self):
        self.get_link_to_course().send_keys(self.link_to_course)
        print("ввод ссылки на курс")

    def click_select_regionalCourse(self):
        self.get_regionalCourse().click()
        print("клик на выпадающий список выбора региональный или нет")

    def click_select_seller(self):
        self.get_seller().click()
        print("клик на выпадающий список выбора продавца")

    def click_auto_send_document(self):
        self.get_auto_send_document().click()
        print("клик на выпадающий список выбора авто отправки договора")

    def input_discount_member_akpp(self):
        self.get_discount_member_akpp().send_keys('10')
        print("ввод значения скидки за членство в акпп")

    def input_discount_full_cource(self):
        self.get_discount_full_cource().send_keys('10')
        print("ввод значения скидки за покупку курса")

    def input_lead_plan(self):
        self.get_lead_plan().send_keys('200')
        print("ввод значения план лиды")

    def input_date_start_RK(self):
        self.get_date_start_RK().send_keys("11.10.2023")
        print("ввод даты старта рекламной компании")

    def input_min_count_people(self):
        self.get_min_count_people().send_keys("10")
        print("ввод минимального кол-во участников")

    def input_activity_end_date(self):
        self.get_activity_end_date().send_keys("31.10.2023")
        print("ввод даты окончания активности")

    def input_sdo(self):
        self.get_sdo().send_keys("")
        print("ввод данных о СДО")

    def input_academic_hours(self):
        self.get_academic_hours().send_keys("100")
        print("ввод академических часов")

    def input_all_tin(self):
        self.get_all_tin().send_keys("100")
        print("ввод кол-во ТиНов")

    def input_all_int(self):
        self.get_all_int().send_keys("100")
        print("ввод кол-во интервизий")

    def input_seminar_attendance(self):
        self.get_seminar_attendance().send_keys("80")
        print("ввод кол-во % для Посещаемости семинаров")

    def input_attendance_ind_supervision(self):
        self.get_attendance_ind_supervision().send_keys("100")
        print("ввод кол-во % для посещаемости инд. супервизий (БК)")

    def input_progress_ind_supervision(self):
        self.get_progress_ind_supervision().send_keys("100")
        print("ввод кол-во % для успеваемости инд. супервизий")

    def input_attendance_tin(self):
        self.get_attendance_tin().send_keys("100")
        print("ввод кол-во % для посещаемости (успеваемости) ТиНов")

    def input_attendance_int(self):
        self.get_attendance_int().send_keys("100")
        print("ввод кол-во % для посещаемости интервизий")

    def input_group_supervision(self):
        self.get_group_supervision().send_keys("100")
        print("ввод кол-во % для посещаемости групповых супервизий")

    def input_final_testing_seminar(self):
        self.get_final_testing_seminar().send_keys("100")
        print("ввод кол-во единиц для итогового тестирование посеминарно")

    def click_performance_for_sertificat(self):
        self.get_performance_for_sertificat().click()
        print("клик на выпадающее меню Необходимая успеваемость для сертификата: ")

    def click_itog_supervision(self):
        self.get_itog_supervision().click()
        print("клик на выпадающее меню Необходимая успеваемость для допуска к итоговой супервизии:")

    def input_seminar_attendance_supervision(self):
        self.get_seminar_attendance_supervision().send_keys("100")
        print("ввод кол-во % Посещаемость семинаров для допуска к итог супервизии")

    def input_attendance_ind_supervision_supervision(self):
        self.get_attendance_ind_supervision_supervision().send_keys("100")
        print("ввод кол-во % Посещаемость инд. супервизий (БК) для допуска к итог супервизии")

    def input_progress_ind_supervision_supervision(self):
        self.get_progress_ind_supervision_supervision().send_keys("100")
        print("ввод кол-во % Успеваемость инд. супервизий  для допуска к итог супервизии")

    def input_attendance_tin_supervision(self):
        self.get_attendance_tin_supervision().send_keys("100")
        print("ввод кол-во % Посещаемость (успеваемость) Тины  для допуска к итог супервизии")

    def input_attendance_int_supervision(self):
        self.get_attendance_int_supervision().send_keys("100")
        print("ввод кол-во % Интервизии посещаемость  для допуска к итог супервизии")

    def input_group_supervision_supervision(self):
        self.get_group_supervision_supervision().send_keys("100")
        print("ввод кол-во % Групповые супервизии посещаемость для допуска к итог супервизии")

    def input_final_testing_seminar_supervision(self):
        self.get_final_testing_seminar_supervision().send_keys("100")
        print("ввод кол-во % Итоговое тестирование посеминарное для допуска к итог супервизии")

    def input_sert_group_supervision(self):
        self.get_sert_group_supervision().send_keys("100")
        print("ввод кол-во % в поле Выдаётся сертификат за посещение N уникальных гр.супервизий")

    def input_link_brif(self):
        self.get_link_brif().send_keys("link_brif")
        print("ввод ссылки на Бриф")

    def input_link_passport(self):
        self.get_link_passport().send_keys("test link pasport")
        print("ввод ссылки на паспорт")

    def input_promotion(self):
        self.get_promotion().send_keys("100")
        print("ввод значения акции")

    def input_promotion_description(self):
        self.get_promotion_description().send_keys("promotion_description")
        print("ввод описания акции")

    def input_short_description_course(self):
        self.get_short_description_course().send_keys("short_description_course")
        print("ввод короткого описания акции")

    def input_description_course(self):
        self.get_description_course().send_keys("description_course")
        print("ввод описания курса")

    def input_target_course(self):
        self.get_target_course().send_keys("target_course")
        print("ввод цели курса")

    def click_button_add_field_advantages_of_course(self):
        self.get_button_add_field_advantages_of_course().click()
        print("клик на кнопку добавить поле преимущества программы")

    def input_title_advantages_of_course(self):
        self.get_title_advantages_of_course().send_keys("title_advantages_of_course")
        print("ввод заголовка преимущества программы")

    def input_text_advantages_of_course(self):
        self.get_text_title_advantages_of_course().send_keys("text_advantages_of_course")
        print("ввод текста преимущества программы")

    def click_delete_button_advantages_of_course(self):
        self.get_delete_button_advantages_of_course().click()
        print("удаления поле заголовок и текст преимущест программы")

    def input_link_video_vizitka(self):
        self.get_link_video_vizitka().send_keys("link_video_vizitka")
        print("ввод ссылки на видео визитку")

    def click_button_add_field_program_suitable(self):
        self.get_button_add_field_program_suitable().click()
        print("клик на кнопку добавить поле кому подойдёт программа")

    def input_title_program_suitable(self):
        self.get_title_program_suitable().send_keys("title_program_suitable")
        print("ввод заголовка кому подойдёт программа")

    def input_text_program_suitable(self):
        self.get_text_program_suitable().send_keys("text_program_suitable")
        print("ввод текста кому подойдёт программа")

    def input_learning_results(self):
        self.get_learning_results().send_keys("learning_results")
        print("ввод результатов обучения")

    def click_button_add_field_videofeedback(self):
        self.get_button_add_field_videofeedback().click()
        print("клик на кнопку добавить поле видеоозывы")

    def input_link_viodeofeedback(self):
        self.get_link_viodeofeedback().send_keys("link_viodeofeedback")
        print("ввод ссылки на видеоотзывы")

    def input_conditions_take_part(self):
        self.get_conditions_take_part().send_keys("conditions_take_part")
        print("ввод условий участия")

    def input_description_course_speakers(self):
        self.get_description_course_speakers().send_keys("description_course_speakers")
        print("ввод общего описание спикеров курса")

    def click_button_add_field_feedback(self):
        self.get_button_add_field_feedback().click()
        print("клик на кнопку добавить поле отзывы")

    def input_filed_of_FIO(self):
        self.get_filed_of_FIO().send_keys("filed_of_FIO")
        print("ввод ФИО")

    def input_filed_of_feedback(self):
        self.get_filed_of_feedback().send_keys("filed_of_feedback")
        print("ввод отзыва")

    def input_filed_of_cashback(self):
        self.get_filed_of_cashback().send_keys("100")
        print("ввод количества кешбека")

    def click_button_add_course(self):
        self.get_button_add_course().click()
        print("клик на кнопку добавить курс")

    # Methods
    def create_new_course(self):
        time.sleep(5)
        self.get_current_url()
        self.iframe()
        time.sleep(5)
        self.click_add_courses()
        self.input_course_name()
        self.click_cancel_sending_email()
        self.input_short_name_course()
        self.input_date_start_course()
        self.input_date_stop_course()
        self.input_course_version()
        self.input_potok()

        select_element_type_of_course = (By.XPATH, self.select_type_course)
        self.select_option_by_visible_text(select_element_type_of_course, self.dict_type_of_course['БК'])

        select_element_difficulty_of_course = (By.XPATH, self.select_difficulty_of_course)
        self.select_option_by_visible_text(select_element_difficulty_of_course, self.difficulty[2])

        self.input_link_to_course()

        select_element_regionalCourse = (By.XPATH, self.select_regionalCourse)
        self.select_option_by_visible_text(select_element_regionalCourse, self.yes_or_not['Да'])

        select_element_seller = (By.XPATH, self.seller)
        self.select_option_by_visible_text(select_element_seller, self.dict_seller['АКППcbt'])

        select_element_auto_send_document = (By.XPATH, self.auto_send_document)
        self.select_option_by_visible_text(select_element_auto_send_document, self.yes_or_not['Да'])

        self.clear_value_fields(self.discount_member_akpp)
        self.input(self.discount_member_akpp, self.test_date['date_discount_member_akpp'])
        self.clear_value_fields(self.discount_full_cource)
        self.input(self.discount_member_akpp, self.test_date['date_discount_full_cource'])

        self.input_lead_plan()
        self.input_date_start_RK()
        self.input_min_count_people()
        self.input_activity_end_date()
        self.input_academic_hours()

        select_element_who_issues_certificates = (By.XPATH, self.who_issues_certificates)
        self.select_option_by_visible_text(select_element_who_issues_certificates, self.dict_who_issues_certificates['АКПП'])

        select_element_all_seminars = (By.XPATH, self.all_seminars)
        self.select_option_by_visible_text(select_element_all_seminars, self.yes_or_not['Да'])

        self.input_all_tin()
        self.input_all_int()

        select_element_sert_course = (By.XPATH, self.sert_course)
        self.select_option_by_visible_text(select_element_sert_course, self.yes_or_not['Да'])

        select_element_diplom_profy = (By.XPATH, self.diplom_profy)
        self.select_option_by_visible_text(select_element_diplom_profy, self.yes_or_not['Да'])

        select_element_udostoverenie_kurs = (By.XPATH, self.udostoverenie_kurs)
        self.select_option_by_visible_text(select_element_udostoverenie_kurs, self.yes_or_not['Да'])

        select_element_sert_all_seminar = (By.XPATH, self.sert_all_seminar)
        self.select_option_by_visible_text(select_element_sert_all_seminar, self.yes_or_not['Да'])

        select_element_sert_otd_seminar = (By.XPATH, self.sert_otd_seminar)
        self.select_option_by_visible_text(select_element_sert_otd_seminar, self.yes_or_not['Да'])

        self.clear_value_fields(self.seminar_attendance)
        self.input_seminar_attendance()
        self.clear_value_fields(self.attendance_ind_supervision)
        self.input_attendance_ind_supervision()
        self.clear_value_fields(self.progress_ind_supervision)
        self.input_progress_ind_supervision()
        self.clear_value_fields(self.attendance_tin)
        self.input_attendance_tin()
        self.clear_value_fields(self.attendance_int)
        self.input_attendance_int()
        self.clear_value_fields(self.group_supervision)
        self.input_group_supervision()
        self.clear_value_fields(self.final_testing_seminar)
        self.input_final_testing_seminar()

        self.click_performance_for_sertificat()

        self.click_itog_supervision()

        self.clear_value_fields(self.seminar_attendance_supervision)
        self.input_seminar_attendance_supervision()
        self.clear_value_fields(self.attendance_ind_supervision_supervision)
        self.input_attendance_ind_supervision_supervision()
        self.clear_value_fields(self.progress_ind_supervision_supervision)
        self.input_progress_ind_supervision_supervision()
        self.clear_value_fields(self.attendance_tin_supervision)
        self.input_attendance_tin_supervision()
        self.clear_value_fields(self.attendance_int_supervision)
        self.input_attendance_int_supervision()
        self.clear_value_fields(self.group_supervision_supervision)
        self.input_group_supervision_supervision()
        self.clear_value_fields(self.final_testing_seminar_supervision)
        self.input_final_testing_seminar_supervision()
        time.sleep(2)
        self.click_itog_supervision()
        self.clear_value_fields(self.sert_group_supervision)
        self.input_sert_group_supervision()
        self.input_link_brif()
        self.input_link_passport()

        select_element_department = (By.XPATH, self.department)
        self.select_option_by_visible_text(select_element_department, self.dict_department['НТ'])

        self.clear_value_fields(self.promotion)
        self.input_promotion()
        self.input_promotion_description()
        self.input_short_description_course()
        self.input_description_course()
        self.input_target_course()
        time.sleep(1)
        self.click_button_add_field_advantages_of_course()
        self.input_title_advantages_of_course()
        self.input_text_advantages_of_course()
        # self.click_delete_button_advantages_of_course()
        self.input_link_video_vizitka()
        self.click_button_add_field_program_suitable()
        self.input_title_program_suitable()
        self.input_text_program_suitable()
        self.input_learning_results()
        self.click_button_add_field_videofeedback()
        # self.input_link_viodeofeedback()
        self.input_conditions_take_part()
        self.input_description_course_speakers()
        self.click_button_add_field_feedback()
        self.input_filed_of_FIO()
        self.input_filed_of_feedback()
        self.clear_value_fields(self.filed_of_cashback)
        self.input_filed_of_cashback()
        self.click_button_add_course()
        time.sleep(3)
        self.switch_to_alert()
        time.sleep(3)
