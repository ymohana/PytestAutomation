from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_Demo():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    searchBox = driver.find_element(By.NAME, "q")
    searchBox.send_keys("pytest selenium" + Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.title_contains("pytest selenium"))
    assert "pytest selenium" in driver.title
    driver.quit()

def test_lambda(): 
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.lambdatest.com/selenium")
    titleName = driver.title
    assert titleName == "What Is Selenium? Getting Started With Selenium Testing | LambdaTest"




