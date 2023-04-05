import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import assertpy

class AppiumIosConfig:
    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            # Set URL of the application under test
            "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
            # Specify device and os_version for testing
            "deviceName": "samsung galaxy m53",
            "platformVersion": "13",
            # Set other BrowserStack capabilities
            "bstack:options": {
                "userName": "prateek_yC5L8S",
                "accessKey": "VfNZWpzp2p1Ch8TtfJZZ",
                "projectName": "python_project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test"
            }
        }

        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestSampleApp(AppiumIosConfig):
    def test_text_box(self):
        self.driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="Text"]').click()

        self.driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeTextField[@name="Text Input"]').send_keys("Helino")
        #self.driver.back()

        self.driver.find_element(AppiumBy.XPATH,'(//XCUIElementTypeButton[@name="UI Elements"])[1]').click()

        #Click on Alert

        self.driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="Alert"]').click()

        #get the text and assert - This is a native alert.

        alert = self.driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="This is a native alert."]').text
        print(alert)

        assertpy.assert_that("This is a native alert.").is_equal_to(alert)

        self.driver.find_element(AppiumBy.XPATH, '// XCUIElementTypeButton[@name = "OK"]').click()