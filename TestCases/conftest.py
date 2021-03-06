import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver= webdriver.Chrome("C://chromedriver.exe")
        print("Launching chrome browser______")
    elif browser == "firefox":
        driver = webdriver.Firefox("C://geckodriver.exe")
        print("Launching firefox browser______")
    else:
        driver = webdriver.Edge()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'IMDb project'
    config._metadata['Module Name'] = 'Clients'
    config._metadata['Tester'] = 'Sinchana'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
