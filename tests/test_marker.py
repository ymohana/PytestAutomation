import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
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


    