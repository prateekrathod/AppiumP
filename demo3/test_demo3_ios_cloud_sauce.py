import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import assertpy
from assertpy import assert_that


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
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("admin")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "admin123")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()
        actual_error = self.driver.find_element(AppiumBy.XPATH,
                                                "//XCUIElementTypeStaticText[contains(@name,'not match')]").text
        assert_that(actual_error).contains("Username and password do not match")

    def test_add_to_cart(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()

        # add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()

        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()
        # swipe and click on checkout
        print(len(self.driver.find_elements(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']")))
        print(self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed())

        size_dic = self.driver.get_window_size()
        x1 = size_dic['width'] * (50 / 100)
        y1 = size_dic['height'] * (75 / 100)

        x2 = size_dic['width'] * (50 / 100)
        y2 = size_dic['height'] * (25 / 100)

        while not self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed():
            self.driver.swipe(x1, y1, x2, y2, 1000)

        self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()

    def test_add_to_cart_mobile_command(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()

        # add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()

        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()
        # swipe and click on checkout
        print(len(self.driver.find_elements(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']")))
        print(self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed())

        # swipe based on visiblity
        while not self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed():
            self.driver.execute_script("mobile: scroll", {"direction": "down"})

        self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()

    def test_add_to_cart_mobile_command_method4(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()

        # add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()

        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()

        para_dic = {"direction":"down","predicateString":"name==test-CHECKOUT","toVisible":True}

        self.driver.execute_script("mobile:scroll", para_dic)
        self.driver.execute_script("mobile:scroll", {"direction":'down'})

        self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()

