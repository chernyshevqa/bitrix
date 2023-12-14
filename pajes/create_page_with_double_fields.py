import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from test_data.data_test import*
"""Главная страница сайта"""


class Create_new_course_lending_x2(Base):
    url = 'https://auth2.bitrix24.net/oauth/authorize/?user_lang=ru&client_id=b24.602d16f604c2d8.45796162&redirect_uri=https%3A%2F%2Fbecbt.bitrix24.ru%2Fauth%2F%3Fauth_service_id%3DBitrix24Net%26sessid%3D788e09a7fb14be58395b29dadb9fa32b%26backurl%3D%252Fcompany%252Fpersonal%252Fuser%252F4040%252Ftasks%252F&scope=auth,profile&response_type=code&mode=page&state=site_id%3Ds1%26backurl%3D%252Fauth%252F%253Fcheck_key%253Dbd687a380c23ef3e4ed4429af603c213%2526backurl%253D%25252Fcompany%25252Fpersonal%25252Fuser%25252F4040%25252Ftasks%25252F%26mode%3Dpage&logout=yes'

    def __init__(self, driver):
        super().__init__(driver, WebDriverWait(driver, 10))
        self.driver = driver

    # Locators
    performance_for_sertificat = (By.XPATH, "//*[contains(text(), 'Необходимая успеваемость для сертификата:')]")
    add_courses = (By.XPATH, "//button[@class='button_ok openAddCourse']")
    course_name = (By.XPATH, "//input[@id='nameCourse']")
    search_courses = (By.XPATH, "//input[@id='name_сourse_search']")
    cancel_sending_email = (By.XPATH, "//input[@id='сancelSendingEmails']")
    short_name_course = (By.XPATH, "//input[@id='shortNameCourse']")
    date_start_course = (By.XPATH, "//input[@id='dateStartCourse']")
    date_stop_course = (By.XPATH, "//input[@id='dateStopCourse']")
    course_version = (By.XPATH, "//input[@id='verCourse']")
    potok = (By.XPATH, "//input[@id='parentStreamCourse']")
    select_type_course = "//select[@id='type_course_package']"
    select_difficulty_of_course = "//select[@id='difficulty']"
    filed_link_to_course = (By.XPATH, "//input[@id='linkCourse']")
    select_regionalCourse = "//select[@id='regionalCourse']"
    seller = "//select[@id='seller']"
    auto_send_document = "//select[@id='auto_send_document']"
    discount_member_akpp = (By.XPATH, "//input[@id='discountMemberAkpp']")
    discount_full_cource = (By.XPATH, "//input[@id='discountFullCource']")
    lead_plan = (By.XPATH, "//input[@id='leadPlan']")
    date_start_RK = (By.XPATH, "//input[@id='dateStartRK']")
    min_count_people = (By.XPATH, "//input[@id='mincountpeople']")
    activity_end_date = (By.XPATH, "//input[@id='activity_end_date']")
    sdo = (By.XPATH, "//input[@id='sdo']")
    academic_hours = (By.XPATH, "//input[@id='academichours']")
    # add_pictires = (By.XPATH, "(//span[contains(text(),'Выбрать обложку')])[1]")
    who_issues_certificates = "//select[@id='who_issues_certificates']"
    all_seminars = "//select[@id='all_seminars']"
    all_tin = (By.XPATH, "//input[@id='all_tin']")
    all_intervision = (By.XPATH, "//input[@id='all_int']")
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
    fields_of_sertification = (
        By.XPATH, "(//div[contains(text(),'Сертификация и успеваемость:')])[1]")
    attendance_ind_supervision_supervision = (By.XPATH, "//input[@id='attendance_ind_supervision_supervizii']")
    progress_ind_supervision_supervision = (By.XPATH, "//input[@id='progress_ind_supervision_supervizii']")
    attendance_tin_supervision = (By.XPATH, "//input[@id='attendance_tin_supervizii']")
    attendance_int_supervision = (By.XPATH, "//input[@id='attendance_int_supervizii']")
    group_supervision_supervision = (By.XPATH, "//input[@id='group_supervizii_supervizii']")
    final_testing_seminar_supervision = (By.XPATH, "//input[@id='final_testing_seminar_supervizii']")

    """Доп информация для формирования страниц"""
    button_extra_information_for_pagers = (
        By.XPATH, "(//div[contains(text(),'Доп информация для формирования страниц:')])[1]")
    sert_group_supervision = (By.XPATH, "//input[@id='sert_group_supervizii']")
    link_brif = (By.XPATH, "//input[@id='link_brif']")
    link_passport = (By.XPATH, "//input[@id='link_passport']")
    button_open_sertification = (By.XPATH, "//*[contains(text(), 'Сертификаты:')]")
    button_add_oblojka = (By.XPATH, "//input[@id='imageCover']")
    button_add_illustration = (By.XPATH, "//input[@id='imageIllustration']")
    department = "//select[@id='department']"
    promotion = (By.XPATH, "//input[@id='promotion']")
    promotion_description = (By.XPATH, "//textarea[@id='promotion_str']")
    description_course = (By.XPATH, "//textarea[@id='description_course']")
    short_description_course = (By.XPATH, "//textarea[@id='sokr_description_course']")
    button_target_course = (By.XPATH,
                            '//button[@onclick="createFieldTargetCourse(document.getElementsByClassName(\'program-container-target_course\')[0])"]')
    target_course = "(//input[@placeholder='Заголовок'])"
    button_add_field_advantages_of_course = (By.XPATH,
                                             '//button[@onclick="createField(document.getElementsByClassName(\'program-container-benefits_program\')[0])"]')
    title_advantages_of_course = "(//div[@class='program-item program-item--adv program-item--adv-benefits_program']//input[@placeholder='Заголовок'])"
    text_advantages_of_course = "(//div[@class='program-item program-item--adv program-item--adv-benefits_program']//textarea[@placeholder='Текст'])"
    delete_button_advantages_of_course = (By.XPATH,
                                          "//div[@class='program-item program-item--adv program-item--adv-benefits_program']//i[@class='fa fa-trash']")
    link_video_vizitka = (By.XPATH, "//input[@id='link_video_vizit']")
    button_add_field_program_suitable = (By.XPATH,
                                         '//button[@onclick="createFieldProgramSuitable(document.getElementsByClassName(\'program-container-program_suitable\')[0])"]')
    title_program_suitable ="(//div[@class='program-container program-container-program_suitable']//input[@placeholder='Заголовок'])"
    text_program_suitable = "(//div[@class='program-container program-container-program_suitable']//textarea[@placeholder='Текст'])"
    button_add_learning_results = (By.XPATH, "//button[@onclick='renderFieldLearningOutcomes()']")
    button_add_photo_learning_results = (By.XPATH, "(//span[contains(text(),'Добавить фото')])[1]")
    learning_results_title = "(//div[@class='learning_outcomes-container']//input[@placeholder='Заголовок'])"
    learning_results_text = "(//div[@class='learning_outcomes-container']//textarea[@placeholder='Текст'])"
    button_add_field_videofeedback = (By.XPATH,
                                      '//button[@onclick="createFieldVideoReviews(document.getElementsByClassName(\'program-container-video_reviews\')[0])"]')
    link_viodeofeedback ="(//div[@class='program-container program-container-video_reviews']//input[@placeholder='Ссылка'])"
    button_conditions_take_part = (By.XPATH,
                                   '//button[@onclick="createFieldTermsParticipation(document.getElementsByClassName(\'program-container-terms_participation\')[0])"]')
    conditions_take_part = "(//div[@class='program-container program-container-terms_participation']//input[@placeholder='Заголовок'])"
    description_course_speakers = (By.XPATH, "//textarea[@id='description_course_speakers']")
    button_add_field_feedback = (By.XPATH, "//button[@onclick='renderFieldReview()']")
    button_add_photo_feedback = (By.XPATH, "//div[@class='review-container']//span[contains(text(),'Добавить фото')][1]")
    filed_of_FIO = "(//div[@class='review-item']//input[@placeholder='ФИО'])"
    filed_of_feedback = "(//div[@class='review-item']//textarea[@placeholder='Отзыв2'])"
    lending = (By.XPATH, "//select[@id='generate_lending']")
    autopay = (By.XPATH, "//select[@id='autopay']")
    description_course_programm = (By.XPATH, "//input[@id='description_program']")
    prise_course = (By.XPATH, "//input[@id='price_course']")
    info_sertification = (By.XPATH, "//textarea[@id='info_sert']")
    button_add_field_FAQ = By.XPATH, '//button[@onclick="createFieldFaq(document.getElementsByClassName(\'program-container-faq\')[0])"]'
    FAQ_title = "(//div[@class='program-item program-item--adv program-item--adv-faq']//input[@placeholder='Заголовок'])"
    FAQ_text = "(//div[@class='program-item program-item--adv program-item--adv-faq']//textarea[@placeholder='Текст'])"
    filed_of_cashback = (By.XPATH, "//input[@id='kaschback']")
    button_add_course = (By.XPATH, "//button[@id='addCourse']")
    errors = (By.XPATH, "//p[@class='mess_error_course']")

    # Getters

    def iframe(self):
        return WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='app-frame']")))

    # Methods
    def create_new_course(self):
        time.sleep(5)
        self.get_current_url()
        self.iframe()
        time.sleep(5)
        self.click(self.add_courses)
        """необходимая инфа для создания курса"""
        self.input(self.course_name, test_date['date_course_name'])
        self.click(self.cancel_sending_email)
        self.input(self.short_name_course, test_date['date_short_name_course'])
        self.input(self.date_start_course, test_date['date_start_course'])
        self.input(self.date_stop_course, test_date['date_stop_course'])
        self.input(self.course_version, test_date['date_course_version'])
        self.input(self.potok, test_date['date_potok'])

        select_element_type_of_course = (By.XPATH, self.select_type_course)
        self.select_option_by_visible_text(select_element_type_of_course, dict_type_of_course['БК'])

        select_element_difficulty_of_course = (By.XPATH, self.select_difficulty_of_course)
        self.select_option_by_visible_text(select_element_difficulty_of_course, difficulty[2])

        self.input(self.filed_link_to_course, test_date['date_link_to_course'])

        select_element_regionalCourse = (By.XPATH, self.select_regionalCourse)
        self.select_option_by_visible_text(select_element_regionalCourse, yes_or_not['Да'])

        select_element_seller = (By.XPATH, self.seller)
        self.select_option_by_visible_text(select_element_seller, dict_seller['АКППcbt'])

        select_element_auto_send_document = (By.XPATH, self.auto_send_document)
        self.select_option_by_visible_text(select_element_auto_send_document, yes_or_not['Да'])

        self.clear_value_fields(self.discount_member_akpp)
        self.input(self.discount_member_akpp, test_date['date_discount_member_akpp'])
        self.clear_value_fields(self.discount_full_cource)
        self.input(self.discount_full_cource, test_date['date_discount_full_cource'])

        self.input(self.lead_plan, test_date['date_lead_plan'])
        self.input(self.date_start_RK, test_date['date_start_RK'])
        self.input(self.min_count_people, test_date['date_min_count_people'])
        self.input(self.activity_end_date, test_date['date_activity_end_date'])
        self.input(self.academic_hours, test_date['date_academic_hours'])
        select_element_department = (By.XPATH, self.department)
        self.select_option_by_visible_text(select_element_department, dict_department['НТ'])
        self.input(self.link_brif, test_date['date_link_brif'])
        self.input(self.link_passport, test_date['date_link_passport'])
        # self.input(self.button_add_oblojka, r"D:\testing\Becbt-online\Тестданные\3ce740d01fcc48ac8a3bd42a01ff.jpg"), print("123")
        # self.click(self.button_open_sertification)

        """раздел Доп информация для формирования страниц"""
        self.click(self.button_extra_information_for_pagers), print("click on the button")
        time.sleep(3)
        self.clear_value_fields(self.promotion)
        self.input(self.promotion, test_date['date_promotion'])
        self.input(self.promotion_description, test_date['date_promotion_description'])
        self.input(self.short_description_course, test_date['date_short_description_course'])
        time.sleep(1)
        self.input(self.description_course, test_date['date_description_course'])
        self.add_extra_field(3, self.button_target_course, self.target_course, test_date['date_target_course'])
        time.sleep(3)
        self.input(self.description_course_speakers, test_date['date_description_course_speakers'])
        self.add_extra_fields(2, self.button_add_field_feedback, self.filed_of_FIO, self.filed_of_feedback,
                              test_date['date_filed_of_FIO'], test_date['date_filed_of_feedback'])
        self.select_option_by_visible_text(self.autopay, yes_or_not['Да'])
        self.add_extra_fields(3, self.button_add_field_advantages_of_course, self.title_advantages_of_course,
                              self.text_advantages_of_course, test_date['date_title_advantages_of_course'],
                              test_date['date_text_advantages_of_course'])
        # self.click_delete_button_advantages_of_course()
        self.input(self.link_video_vizitka, test_date['date_link_video_vizitka'])
        self.add_extra_fields(3, self.button_add_field_program_suitable, self.title_program_suitable,
                              self.text_program_suitable, test_date['date_title_program_suitable'],
                              test_date['date_text_program_suitable'])
        self.add_extra_fields(3, self.button_add_learning_results, self.learning_results_title,
                              self.learning_results_text, test_date['date_learning_results'],
                              test_date['date_learning_results'])
        # self.input(self.button_add_photo_learning_results, "D:\\testing\\Becbt-online\\Тестданные")
        self.add_extra_field(2, self.button_add_field_videofeedback, self.link_viodeofeedback,
                             test_date['date_link_viodeofeedback'])
        self.add_extra_field(3, self.button_conditions_take_part, self.conditions_take_part,
                             test_date['date_conditions_take_part'])
        # self.input(self.button_add_photo_feedback, "D:\\testing\\Becbt-online\\Тестданные")
        self.input(self.description_course_programm, test_date['date_description_course_programm'])
        self.clear_value_fields(self.prise_course)
        self.input(self.prise_course, test_date['date_prise_course'])
        self.add_extra_fields(3, self.button_add_field_FAQ, self.FAQ_title,
                              self.FAQ_text,test_date['date_FAQ_title'],
                              test_date['date_FAQ_text'])
        self.clear_value_fields(self.filed_of_cashback)
        self.input(self.filed_of_cashback, test_date['date_filed_of_cashback'])
        self.select_option_by_visible_text(self.lending, yes_or_not['Да'])
        #
        """раздел Сертификация"""
        self.click(self.fields_of_sertification)
        select_element_who_issues_certificates = (By.XPATH, self.who_issues_certificates)
        self.select_option_by_visible_text(select_element_who_issues_certificates,
                                           dict_who_issues_certificates['АКПП'])

        select_element_all_seminars = (By.XPATH, self.all_seminars)
        self.select_option_by_visible_text(select_element_all_seminars, yes_or_not['Да'])
        self.input(self.all_tin, test_date['date_all_tin'])
        self.input(self.all_intervision, test_date['date_all_intervision'])
        select_element_sert_course = (By.XPATH, self.sert_course)
        self.select_option_by_visible_text(select_element_sert_course, yes_or_not['Да'])
        select_element_diplom_profy = (By.XPATH, self.diplom_profy)
        self.select_option_by_visible_text(select_element_diplom_profy, yes_or_not['Да'])
        select_element_udostoverenie_kurs = (By.XPATH, self.udostoverenie_kurs)
        self.select_option_by_visible_text(select_element_udostoverenie_kurs, yes_or_not['Да'])
        select_element_sert_all_seminar = (By.XPATH, self.sert_all_seminar)
        self.select_option_by_visible_text(select_element_sert_all_seminar, yes_or_not['Да'])
        select_element_sert_otd_seminar = (By.XPATH, self.sert_otd_seminar)
        self.select_option_by_visible_text(select_element_sert_otd_seminar, yes_or_not['Да'])
        #
        """Посещаемость столбец 1"""
        self.clear_value_fields(self.seminar_attendance)
        self.input(self.seminar_attendance, test_date['date_seminar_attendance'])
        self.clear_value_fields(self.attendance_ind_supervision)
        self.input(self.attendance_ind_supervision, test_date['date_attendance_ind_supervision'])
        self.clear_value_fields(self.progress_ind_supervision)
        self.input(self.progress_ind_supervision, test_date['date_progress_ind_supervision'])
        self.clear_value_fields(self.attendance_tin)
        self.input(self.attendance_tin, test_date['date_attendance_tin'])
        self.clear_value_fields(self.attendance_int)
        self.input(self.attendance_int, test_date['date_attendance_int'])
        self.clear_value_fields(self.group_supervision)
        self.input(self.group_supervision, test_date['date_group_supervision'])
        self.clear_value_fields(self.final_testing_seminar)
        self.input(self.final_testing_seminar, test_date['date_final_testing_seminar'])
        #
        """Посещаемость столбец 2"""
        self.clear_value_fields(self.seminar_attendance_supervision)
        self.input(self.seminar_attendance_supervision, test_date['date_seminar_attendance_supervision'])
        self.clear_value_fields(self.attendance_ind_supervision_supervision)
        self.input(self.attendance_ind_supervision_supervision,
                   test_date['date_attendance_ind_supervision_supervision'])
        self.clear_value_fields(self.progress_ind_supervision_supervision)
        self.input(self.progress_ind_supervision_supervision,
                   test_date['date_progress_ind_supervision_supervision'])
        self.clear_value_fields(self.attendance_tin_supervision)
        self.input(self.attendance_tin_supervision, test_date['date_attendance_tin_supervision'])
        self.clear_value_fields(self.attendance_int_supervision)
        self.input(self.attendance_int_supervision, test_date['date_attendance_int_supervision'])
        self.clear_value_fields(self.group_supervision_supervision)
        self.input(self.group_supervision_supervision, test_date['date_group_supervision_supervision'])
        self.clear_value_fields(self.final_testing_seminar_supervision)
        self.input(self.final_testing_seminar_supervision, test_date['date_final_testing_seminar_supervision'])
        self.clear_value_fields(self.sert_group_supervision)
        self.input(self.sert_group_supervision, test_date['date_sert_group_supervision'])
        # # self.input(self.button_add_oblojka, "D:\\testing\\Becbt-online\\Тестданные")
        self.click(self.button_add_course), print("нажать на кнопку добавить")
        self.get_error_value(dict_errors)
        self.switch_to_alert()
