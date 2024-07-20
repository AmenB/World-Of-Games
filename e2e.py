import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_scores_service():
    chrome_options = ChromiumOptions()

    service = Service(ChromeDriverManager().install(), options=chrome_options)
    driver_chrome = webdriver.Chrome(service=service)

    driver_chrome.get("http://127.0.0.1:8777/")
    score = driver_chrome.find_element(By.ID, "score")
    if int(score.text)>=0 or int(score.text)<=1000:
        return True
    else:
        return False


def main_function():
    if test_scores_service() == True:
        return sys.exit(0)
    else:
        return sys.exit(-1)




main_function()
