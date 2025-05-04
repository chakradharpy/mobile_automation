from appium import webdriver
from appium.options.android import UiAutomator2Options

APK_PATH = r"C:/Users/Chakradhar/Desktop/indee_task/application/hfiPevjjJ1DgrIGU5G3n.apk"

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "65aa65d0"
options.app = APK_PATH
options.automation_name = "UiAutomator2"
options.platform_version = "11"
options.no_reset = True
options.auto_web_view = True              


driver = webdriver.Remote("http://127.0.0.1:4723", options)




 
 
