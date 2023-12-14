import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
import os

base_url = "*"  # замените на ваш реальный URL
base_url_1 = "*"

driver = webdriver.Chrome() 

# # Задаём количество изображений
# num_images = 183

# Создаём список для хранения отсутствующих изображений
missing_images = []

# Перейдите на страницу
driver.get(base_url_1)
driver.maximize_window()
user_name = driver.find_element(By.XPATH, '//*[@name="email"]')
user_name.send_keys("*")
password = driver.find_element(By.ID, "password-field")
password.send_keys("*")
button = driver.find_element(By.ID, "submit")
button.click()
driver.get(base_url)

# Задаём диапазон номеров изображений
start_image_number = 1
end_image_number = 186

time.sleep(2)

for i in range(start_image_number, end_image_number):
    image_filename = f"{str(i).zfill(3)}.JPG"
    image_url = f"/uploads/events/event616/gallery/{image_filename}"

    # Строим XPath выражение с использованием форматирования строк
    xpath_expression = f"//img[@src='{image_url}']"
    # print(xpath_expression)

    try:
        driver.find_element(By.XPATH, xpath_expression)
    except:
        missing_images.append(image_url)
print('\n'.join(missing_images))
print(f"Количество отсутствующих изображений: {len(missing_images)}")
#
# Закроем браузер после использования
driver.quit()
