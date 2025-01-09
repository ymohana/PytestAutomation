import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
    

def test_example(browser):
    browser.get("https://www.google.com")
    assert "Google" == browser.title

def test_simpleForm(browser):
    browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    browser.find_element(By.XPATH, "//input[@id='user-message']").send_keys("Test")
    browser.find_element(By.XPATH, "//button[@id='showInput']").click()
    message = browser.find_element(By.ID, "message").text
    assert message == "Test"