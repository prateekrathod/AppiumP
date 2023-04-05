import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap={
"app" : "bs://49c1c7702fb0154d4cf4459fa38f65e92564a95b",
"platformVersion" : "9.0",
"deviceName" : "Samsung Galaxy m32",
'bstack:options' :
    {
        "projectName" : "Project python 1",
        "buildName" : "browserstack-build-1",
        "sessionName" : "BStack first_test",
        # Set your access credentials
        "userName" : "prateek_yC5L8S",
        "accessKey" : "VfNZWpzp2p1Ch8TtfJZZ"
    }
}

driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)

driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()

print(driver.page_source)

time.sleep(4)
driver.quit()