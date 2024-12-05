import os

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("****test_001_AccountRegistration started****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.logger.info("****Launching Application****")
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.logger.info("****Click on MyAccount ==> Register****")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomString.random_string_generator()+"@gmail.com"
        # self.regpage.setEmail(ReadConfig.getUseremail())
        # self.regpage.setEmail('test1234567890000@gmail.com')
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword(ReadConfig.getPassword())
        self.regpage.setConfirmPassword(ReadConfig.getPassword())
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getConfirmationmsg()
        if self.confmsg == 'Your Account Has Been Created!':
            self.logger.info("****Account Registration is Passed****")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.getcwd())+"\\screenshots\\"+"test_account_reg.png")
            self.logger.error("****Account Registration is Failed****")
            assert False




# test1234567890000@gmail.com
# abcxyz



# test1234567890000@gmail.com
# abcxyz
#pytest -s -v testCases\test_001_AccountRegistration.py
#pytest -s -v --browser edge testCases\test_001_AccountRegistration.py
#pytest -s -v --browser firefox testCases\test_001_AccountRegistration.py
#pytest -s -v -n=3 --browser edge testCases\test_001_AccountRegistration.py