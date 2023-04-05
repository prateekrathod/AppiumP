import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class AppiumConfig:

    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\Users\144139\Downloads\khan-academy-7-3-2.apk",
            "udid":"emulator-5554"
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestArts(AppiumConfig):
    def test_list_sms(self):
        time.sleep(3)
        messages = self.driver.execute_script("mobile:listSms",{"max":1})
        print(messages)