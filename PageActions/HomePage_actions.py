import time

from selenium.webdriver.common.by import By
from pagesObj.HomePage import HomePage

class HomePageActions:
    def __init__(self, driver):
        self.driver = driver

    strToSearch = 'dzbanek'

    def searchTest(self):
        self.driver.find_element(*HomePage.searchIcon).click()
        self.driver.find_element(*HomePage.searchInput).send_keys(*HomePageActions.strToSearch)

        for element in self.driver.find_elements(*HomePage.searchLis):
            if element.text.lower() == (HomePageActions.strToSearch).lower():
                print('=======OK=======')
                break
            else:
                print("Brak takich produktów")
    def newsLetterTest(self):
        self.driver.find_element(*HomePage.newsletterMain)

