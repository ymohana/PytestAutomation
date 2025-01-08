import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.parametrize("url, title", [
    ("https://www.google.com", "Google"),
    ("https://www.bing.com", "Bing"),
])
def test_check_title(url, title):
   service = Service(ChromeDriverManager().install())
   driver = webdriver.Chrome(service=service)
   driver.maximize_window()
   driver.get(url)
   assert title in driver.title
   driver.quit()