import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.nativekey import AndroidKey


class AppiumConfig:

    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "samsung",
            "app": r"C:\Users\144139\Downloads\com.bsl.hyundai_2021-08-09.apk",
            "udid":"emulator-5553"
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestHyundai(AppiumConfig):

    def test_sign_up(self):
        self.driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/permission_deny_button").click()

        self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button").click()

        self.driver.find_element(AppiumBy.ID,"com.bsl.hyundai:id/txt_signup").click()


