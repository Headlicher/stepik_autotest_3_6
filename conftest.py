import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome', help='Choose browser: firefox or chrome')
    parser.addoption("--language", action='store', default ='ru', help='Choose language')

@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    return language


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    print("\nstart browser for test..")
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name must be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
