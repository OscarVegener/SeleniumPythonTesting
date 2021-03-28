from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time, os
from math import log, sin

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    browser.find_element_by_tag_name("button").click()

    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x))

    browser.find_element_by_css_selector("button[type='submit']").click()

    time.sleep(1)

except AssertionError as e:
    print("FAILED")

except Exception as e:
    print(f'Exception: {e}')

finally:
    time.sleep(3)
    browser.quit()
