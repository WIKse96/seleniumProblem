from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self, driver):
        self.driver = driver

    logo = (By.XPATH, "//a[@aria-label='store logo']//img")
    searchIcon = (By.XPATH, "//i[@class='icon-magnifier icons']")
    searchInput = (By.XPATH, "//input[@id='search-input-autocomplate']")
    searchBtn = (By.XPATH, "//button[@title='Szukaj']")
    searchLis = (By.XPATH, "//div[@class='mst-searchautocomplete__wrapper']/div/div/div/ul/li/div/div[@class='title']/a/span")
    newsletterMain = (By.XPATH, "//div[@class='block newsletter']")

    def goHome(self):
        self.driver.get("https://porcelana.pl/")

    def assertions(self):
       assert self.driver.find_element(*HomePage.logo)
       #wszystkie asercje strony głównej DODAĆ PÓŹNIEJ
