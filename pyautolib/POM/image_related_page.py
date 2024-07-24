from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ImageRelatedPage:
    def __init__(self, driver):
        self.driver = driver
        self.__pic_maybe = '//div[@class="graph-guess-word"]/span'
        self.__can_not_find = ('//div[@class="graph-result-card"]/div[contains'
                               '(@class, "graph-noresult graph-container")]')
        self.__current_page_pic = '//div[@class="graph-result-card"]/div[1]//img'

        WebDriverWait(self.driver, 10).until(
            expected_conditions.title_is("百度识图搜索结果")
        )

    def guess_pic(self):
        return self.driver.find_element(By.XPATH, self.__pic_maybe).text

    def open_specific_image(self, order=1):
        self.driver.find_element(By.XPATH, f'//div[@class="graph-result-card"]/div[1]//div[{order}]//img').click()

    def get_image_title(self, order=1):
        return self.driver.find_element(By.XPATH, f'//div[@class="graph-result-card"]/div[1]//'
                                                  f'div[{order}]//div[@class="graph-product-list-desc"]').text

    def get_search_count(self):
        related_pic = self.driver.find_elements(By.XPATH, self.__current_page_pic)
        related_pic_num = len(related_pic)
        return related_pic_num

    def has_result(self):
        try:
            self.driver.find_element(By.XPATH, self.__can_not_find)
            return False
        except NoSuchElementException:
            return True
