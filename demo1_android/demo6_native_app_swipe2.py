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
            "app": r"C:\Users\144139\Downloads\khan-academy-7-3-2.apk",
            "udid":"emulator-5554"
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestArts(AppiumConfig):

    def test_the_himalayas_topics(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        # id is resource-id only
        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        # ACCESSIBILITY_ID is content-desc in android
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Search tab").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']").click()

        self.driver.implicitly_wait(0)
        size_dic = self.driver.get_window_size()

        #print(size_dic)
        x1 = size_dic['width']*(50/100)
        y1 = size_dic['height']*(75/100)

        x2 = size_dic['width']*(50/100)
        y2 = size_dic['height']*(25/100)
        #print(x1)

        # swipe until //android.widget.TextView[@text='Art oF Asia'] presence
        while len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Art of Asia']")) == 0:
            self.driver.swipe(x1, y1, x2, y2, 1000) # not going tow ork with latest appium server

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Art of Asia']").click()

        time.sleep(5)

