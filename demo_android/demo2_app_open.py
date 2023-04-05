import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class AppiumConfig:

    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "samsung",
            "appPackage":"org.khanacademy.android",
            "appActivity":"org.khanacademy.android.ui.library.MainActivity",
            "udid":"emulator-5554"
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestAndroidDeviceLocal(AppiumConfig):

    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH,
                            "//android.widget.EditText[@content-desc='Enter an e-mail address or username']").send_keys(
            "reva")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[contains(@content-desc,'Pass')]").send_keys(
            "reva123")
        # click on sign in
        self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign in'])[2]").click()
        # get the text "There was an issue signing in" and print it
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").text
        print(actual_error)
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").get_attribute("text")
        print(actual_error)

    def test_invalid_sign_up_email_test(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

    #click on setting icon
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.ImageView[@content-desc='Settings']").click()

    # #click on sign in
        self.driver.find_element(AppiumBy.XPATH,"").click()
    # #click on sign up with email

    # #send firstnamea as john
    # #send lastname as peter
    # #send birthday Aug 20, 1995
#    #send password as welcome123
#   #send email as test123
#   #click on create
#   #assert the error message of mail id