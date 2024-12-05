from selenium.webdriver.common.by import By

class MyAccountPage:
    #locator
    lnk_logout_xpath = "//aside//a[text()='Logout']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    #Action method
    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.lnk_logout_xpath).click()