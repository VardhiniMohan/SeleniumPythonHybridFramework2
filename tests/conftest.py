import pytest as pytest
from selenium import webdriver

driver = None


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
