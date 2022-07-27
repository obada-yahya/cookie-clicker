import time
from selenium import webdriver
from selenium.webdriver.common.by import By
path = "C:/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")
start = time.time()
timer = start
while True:
    curr = time.time()
    if curr - start >= 60 * 5:
        break
    if curr - timer >= 10:
        timer = curr
        items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
        items = items[0:8]
        for item in items[::-1]:
            try:
                item.click()
            except Exception:
                pass
    cookie.click()
driver.quit()
