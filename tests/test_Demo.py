from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Demo():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    searchBox = driver.find_element(By.NAME, "q")
    searchBox.send_keys("pytest selenium" + Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.title_contains("pytest selenium"))
    assert "pytest selenium" in driver.title
    driver.quit()

def test_lambda():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.lambdatest.com/selenium")
    titleName = driver.title
    assert titleName == "What Is Selenium? Getting Started With Selenium Testing | LambdaTest"




