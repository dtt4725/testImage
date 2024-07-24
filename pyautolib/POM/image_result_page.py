from selenium.webdriver.common.by import By
import re

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ImageResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.__result_count = '//div[@id="resultInfo"]'
        self.__submit_button = '//input[@type="submit"]'
        self.__image_path = '//ul[contains(@class, "imglist")]/'

        WebDriverWait(self.driver, 10).until(
            expected_conditions.title_contains("百度图片搜索")
        )

    def get_search_count(self):
        related_pic = self.driver.find_element(By.XPATH, self.__result_count).text
        related_pic_num = int(''.join(re.findall(r'\d+', related_pic)))
        return related_pic_num

    def open_image(self, order=0):
        self.driver.find_element(By.XPATH, f"{self.__image_path}li[{order}]").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def get_image_title(self, order=0):
        return self.driver.find_element(By.XPATH, f"{self.__image_path}li[{order}]").get_attribute("data-title")
