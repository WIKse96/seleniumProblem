import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
from webdriver_manager.core.utils import ChromeType


# funkcja odpowiada za konsole. defaultowo jest chrome, moge podac inną przeglądarkę
def pytest_addoption(parser):
    parser.addoption(
        "--cat_url"
        "", action="store", default="https://porcelana.pl/",

    )


# oznaczenie, że poniższa funkcja jest w scope klasy
@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    # pobranie tego co zostało wpisane w konsole
    cat_url = request.config.getoption("cat_url")
    # options.add_argument('--headless')
    options.add_argument('--start-maximized')
    serviceObj = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver = webdriver.Chrome(options=options, service=serviceObj)

    # zadeklarowanie driver w taki sposób aby przekazać go do innego pliku
    driver.get(cat_url)

    driver.implicitly_wait(3)
    request.cls.driver = driver
    # tutaj wykonują się testy, yield to oznacza
    yield

    # po wszystkim na koniec przegladarka się zamyka
    driver.close()
