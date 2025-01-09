import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.mark.parametrize("url, title", [
    ("https://www.google.com", "Google"),
    ("https://www.bing.com", "Bing"),
])
def test_check_title(url, title):
   chrome_options = Options()
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-dev-shm-usage")
   service = Service(executable_path="/usr/bin/chromedriver")
   driver = webdriver.Chrome(service=service, options=chrome_options)
   driver.maximize_window()
   driver.get(url)
   assert title in driver.title
   driver.quit()