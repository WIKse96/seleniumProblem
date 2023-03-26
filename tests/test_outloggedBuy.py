from PageActions.HomePage_actions import HomePageActions
from utilities.BaseClass import BaseClass
from pagesObj.HomePage import HomePage


# @pytest.mark.usefixtures("setup") - dziedziczone z BaseClass
class TestOne(BaseClass):


    def test_OutloggedBuy(self):
        #tworzenie obiektów
        self.driver.get("https://porcelana.pl/")
        homePage = HomePage(self.driver)
        homePage.goHome()

        homePage.assertions()
    def test_search(self):
        homePageActions = HomePageActions(self.driver)
        homePageActions.searchTest()


