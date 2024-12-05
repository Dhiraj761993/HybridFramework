import os
import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.abspath(os.curdir)+"\\testData\\Opencart_LoginData.xlsx"
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login_ddt(self,setup):
        self.logger.info("****Starting of Data Driven Test Case****")
        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        lst_status = []
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()
            self.email = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.targetpage = self.lp.isMyAccountPageExists()

            if self.exp == 'Valid':
                if self.targetpage == True:
                    lst_status.append("Pass")
                    self.ma.clickLogout()
                else:
                    lst_status.append("Fail")
            elif self.exp == 'Invalid':
                if self.targetpage == True:
                    lst_status.append("Fail")
                else:
                    lst_status.append("Pass")

        #final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")


#pytest -s -v -m "sanity" --browser chrome testCases
#pytest -s -v -m "sanity and smoke" --browser chrome testCases





















