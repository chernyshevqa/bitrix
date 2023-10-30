import datetime
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Base():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    """Метод получение текущей юрл"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Corrent url " + get_url)

    """Метод проверки слов"""

    def assert_value_of_product(self, word, result):
        value_word = word.text
        assert value_word == result, f"{value_word}"
        print(result)

    """Метод создания скриншотов"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d - %H.%M.%S")
        self.driver.save_screenshot(f".\\screen\\screenshot{now_date}.png")

    """Метод проверки url"""

    def assert_url(self,result):
        get_url = self.driver.current_url
        assert get_url == result, f"{get_url}"
        print("good url")

        """метод для нажатия стрелки BACKSPACE на клавиатуре"""
    def clear_field(self, element, repeat=2):
        element.send_keys(Keys.BACKSPACE * repeat)

        """метод для нажатия стрелки назад на клавиатуре"""
    def clear_field_arrow_right(self, element, repeat=2):
        element.send_keys(Keys.ARROW_RIGHT * repeat)

        """Метод для работы со списком select"""
    def select_option_by_visible_text(self, locator, value):
        select_element = self.wait.until(EC.visibility_of_element_located(locator))
        select = Select(select_element)
        select.select_by_visible_text(value)


    def get_selected_option_text(self, locator):
        select_element = self.wait.until(EC.visibility_of_element_located(locator))
        selected_option = Select(select_element).first_selected_option
        value = selected_option.text


    """Метод получения локатора iframe"""
    def iframe(self):
        return self.wait.until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='app-frame']")))

    """Метод получения названия курса"""
    def get_text(self, text):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, f"//span[@id='course_name'][text()='{text}']")))
            return True
        except TimeoutException:
            return False

    def switch_to_alert(self):
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Текст всплывающего окна: {alert_text}")
            alert.accept()
        except:
            print("Всплывающее окно не обнаружено")

    def click(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input(self, locator, text):
        return self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    def get_text_1(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def assert_value_select(self, locator, expected_value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        selected_value = Select(element).first_selected_option.get_attribute("value")
        selected_value = element.get_attribute("value")
        assert selected_value == expected_value, f"{selected_value}"

    def assert_value_select_text(self, locator, expected_value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        text_content = element.text.strip()
        assert text_content.startswith(expected_value), f"Expected: {expected_value}, Actual: {text_content}"
        assert text_content == expected_value, f"{text_content}"

    def assert_value_input(self, locator, expected_value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        input_value = element.get_attribute("value")
        assert input_value == expected_value, f"{input_value}"



    def assert_checkbox(self, locator):
        checkbox = self.wait.until(EC.visibility_of_element_located(locator))
        assert checkbox.is_selected()

    def clear_value_fields(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).clear()
