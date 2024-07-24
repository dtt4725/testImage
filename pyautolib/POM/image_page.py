import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pyautolib.POM.image_related_page import ImageRelatedPage
from pyautolib.POM.image_result_page import ImageResultPage
from selenium.webdriver.support import expected_conditions
import pyautogui


class ImagePage:
    def __init__(self, driver):
        self.driver = driver
        self.__website = "https://image.baidu.com/"
        self.__input_box = '//input[@name="word"]'
        self.__submit_button = '//input[@type="submit"]'
        self.__upload_pic = '//i[@class="sc-icon cu-icon"]'
        self.__upload_pic_button = "//div[contains(@class, 'upload-btn')]"

    def open_website(self):
        self.driver.get(self.__website)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.title_is("图搜首页")
        )

    def search_by_word(self, word):
        self.driver.find_element(By.XPATH, self.__input_box).send_keys(word)
        self.driver.find_element(By.XPATH, self.__submit_button).click()
        return ImageResultPage(self.driver)

    def search_by_image(self, image_path):
        self.driver.find_element(By.XPATH, self.__upload_pic).click()
        self.driver.find_element(By.XPATH, self.__upload_pic_button).click()

        # search for the image path on your local env
        time.sleep(5)
        # pyautogui.hold('command')
        pyautogui.keyDown('command')
        pyautogui.press('F')
        pyautogui.keyUp('command')
        time.sleep(2)
        pyautogui.write(image_path)
        time.sleep(2)
        pyautogui.press('enter')

        time.sleep(2)
        pyautogui.press('enter',2)

        time.sleep(10)
        return ImageRelatedPage(self.driver)

