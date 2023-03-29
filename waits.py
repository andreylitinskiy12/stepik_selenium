import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price_100 = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[id='price']"),"$100"))
    btn = browser.find_element(By.CSS_SELECTOR, "[id='book']").click()
    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    y = calc(x)
    text_area = browser.find_element(By.CSS_SELECTOR, "[id='answer']").send_keys(y)
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(10)
finally:
    browser.quit()