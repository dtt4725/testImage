import os
import time

from pyautolib.POM.image_page import ImagePage
from pyautolib.utilities.common import *


# case1
# check if result match the search text in the search box
def atest_search_by_text(driver):
    image_page = ImagePage(driver)
    image_page.open_website()

    # search some text in the text box
    image_result = image_page.search_by_word(os.getenv('SEARCH_WORD'))

    # check if search result count exceed the input number
    related_pic_num = image_result.get_search_count()
    sc_path = os.getenv('SCREENSHOT_PATH')
    check_visit_result = int(os.getenv('VISIT_RESULT'))
    if related_pic_num >= check_visit_result:
        # check if the image title match
        assert string_match(image_result.get_image_title(order=check_visit_result), os.getenv('MATCH_WORD'))
        # take screenshot on origin page
        driver.save_screenshot(f"{sc_path}/case1_{get_timestamp()}.png")
        # open the image
        image_result.open_image(order=check_visit_result)
        time.sleep(5)
        # take screenshot on new page
        driver.save_screenshot(f"{sc_path}/case1_{get_timestamp()}.png")
    else:
        # if there is no enough result , assert fail and take screenshot
        driver.save_screenshot(f"{sc_path}/case1_fail_{get_timestamp()}.png")
        assert False


# case2
# check if result match the uploaded picture
def test_search_by_image(driver):
    image_page = ImagePage(driver)
    image_page.open_website()
    # get the pic path
    image = os.path.abspath(os.path.join(os.path.dirname(__file__), os.getenv('PIC_PATH')))
    # search by the pic
    image_related = image_page.search_by_image(image)

    # check if there are results related to the pic
    assert image_related.has_result()
    check_visit_result = int(os.getenv('VISIT_RESULT'))

    # check if the image title match
    assert string_match(image_related.get_image_title(order=check_visit_result), os.getenv('MATCH_WORD2'))
    # check if the page can guess the pic and show on the top
    assert string_match(image_related.guess_pic(), os.getenv('MATCH_WORD2'))
    sc_path = os.getenv('SCREENSHOT_PATH')
    related_pic_num = image_related.get_search_count()
    if related_pic_num >= check_visit_result:
        # open the match image
        image_related.open_specific_image(order=check_visit_result)
        time.sleep(5)
        # take screenshot
        driver.save_screenshot(f"{sc_path}/case2_{get_timestamp()}.png")
    else:
        # if there is no enough result , assert fail and take screenshot
        driver.save_screenshot(f"{sc_path}/case2_fail_{get_timestamp()}.png")
        assert False
