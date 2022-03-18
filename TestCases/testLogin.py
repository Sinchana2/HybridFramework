import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import Home
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    name = ReadConfig.getName()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    value = 'Release Date'

    logger=LogGen.loggen()

    # @pytest.mark.sanity
    # @pytest.mark.regression
    # def test_signup(self, setup):
    #     self.logger.info("*************** Test_001_Login *****************")
    #     self.logger.info("****Started Login page signup test ****")
    #     self.driver = setup
    #     self.driver.implicitly_wait(100)
    #     self.logger.info("****Opening URL****")
    #     self.driver.get(self.baseURL)
    #     self.driver.implicitly_wait(50)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.signIn(self.name,self.useremail,self.password)
    #     self.hm = Home(self.driver)
    #     page_title = self.hm.get_title()
    #     if page_title == 'IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows':
    #         self.logger.info("****Login test passed ****")
    #         self.driver.close()
    #         assert True
    #     else:
    #         self.logger.error("****Login test failed ****")
    #         self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
    #         self.driver.close()
    #         assert False
    #
    def test_login(self, setup):

        self.driver = setup
        self.hmp = Home(self.driver)

        self.driver.get(ReadConfig.getApplicationURL())
        self.driver.implicitly_wait(20)
        self.hmp.click_on_menu()
        self.driver.implicitly_wait(40)
        self.hmp.click_on_sub_menu()
        self.driver.implicitly_wait(20)
        self.hmp.select_release_date(self.value)


    # @pytest.mark.sanity
    # @pytest.mark.regression
    # def test_homePageTitle(self, setup):
    #     self.logger.info("*************** Test_002_Login *****************")
    #     self.logger.info("****Started Home page title test ****")
    #     self.test_signup(self, setup)
    #     self.hm = Home(self.driver)
    #     self.hm.click_on_menu()
    #     self.hm.click_on_sub_menu()
    #     self.hm.select_release_date(self.value)
    #
    #




