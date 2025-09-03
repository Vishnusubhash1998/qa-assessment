# tests/test_ui_smoke.py
import os
import tempfile
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """
    Chrome WebDriver fixture.
    - Headless by default (required for CI).
    - Set HEADED=1 locally if you want a visible browser.
    - Uses a unique user-data-dir per run to avoid profile conflicts on CI.
    """
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    headed = os.getenv("HEADED", "0") == "1"
    if headed:
        options.add_argument("--start-maximized")
    else:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    # unique profile to avoid "user data directory is already in use"
    temp_profile = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_profile}")

    drv = webdriver.Chrome(service=service, options=options)
    yield drv
    drv.quit()


def test_homepage_title(driver):
    driver.get("https://example.com/")
    assert "Example" in driver.title


def test_find_element_by_data_test(driver):
    driver.get("https://example.com/")
    # example.com has no data-test hooks; assert H1 exists as a smoke check
    h1 = driver.find_element(By.CSS_SELECTOR, "h1")
    assert h1.is_displayed()
