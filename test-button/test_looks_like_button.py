from selenium.webdriver.common.by import By
from pages.looks_like_a_button import LooksLikeAButton



def test_button2_exist(browser):
    looks_like_a_button = LooksLikeAButton(browser)
    looks_like_a_button.open()
    # browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    # assert browser.find_element(By.LINK_TEXT, 'Click').is_displayed()
    assert looks_like_a_button.button_is_displayed()

def test_button2_click(browser):
    looks_like_a_button = LooksLikeAButton(browser)
    looks_like_a_button.open()
    # browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    # browser.find_element(By.LINK_TEXT, 'Click').click()
    looks_like_a_button.button_click()
    # assert 'Submitted' == browser.find_element(By.ID, 'result-text').text
    assert 'Submitted' == looks_like_a_button.result_text()