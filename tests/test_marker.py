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
    
@pytest.mark.login
def test_login_functionality(browser):
    browser.get("https://practicetestautomation.com/practice-test-login/")
    browser.find_element(By.ID, "username").send_keys('student')
    browser.find_element(By.ID, "password").send_keys('Password123')
    browser.find_element(By.ID, "submit").click()
    assert "Logged In Successfully | Practice Test Automation" == browser.title

@pytest.mark.homepage
def test_homepage_functionality(browser):
    browser.get("https://practicetestautomation.com/practice-test-login/")
    browser.find_element(By.LINK_TEXT, "HOME").click()
    assert "Practice Test Automation | Learn Selenium WebDriver" == browser.title
    

    