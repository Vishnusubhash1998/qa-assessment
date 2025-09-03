import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Launch a visible Chrome window
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # comment next line if you want headless
    # options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(service=service, options=options)
    yield drv
    drv.quit()

def test_homepage_title(driver):
    # 🔁 replace this with your real test URL
    url = "https://example.com/"
    driver.get(url)

    # Example assertion: page title contains "Example"
    assert "Example" in driver.title

def test_find_element_by_data_test(driver):
    # 🔁 replace with your real URL that has data-test hooks
    url = "https://example.com/"
    driver.get(url)

    # Example: how to target a data-test hook if present:
    # elem = driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']")
    # elem.click()

    # Since example.com has no hooks, we just assert the H1 exists
    h1 = driver.find_element(By.CSS_SELECTOR, "h1")
    assert h1.is_displayed()
