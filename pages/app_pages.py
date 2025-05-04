from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AppPage:
    def __init__(self, driver):
        self.driver = driver


    def login(self, pin):
        access_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='access-code']"))
        )
        access_code.clear()
        access_code.send_keys(pin)
        sign_in_button = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='sign-in-button']")
        sign_in_button.click()
        time.sleep(3)

    def navigate_to_project(self):
        project_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='Title - Test automation project, ']"))
        )
        project_element.click()
        time.sleep(5)

    def switch_tab(self, tab_name):
        
        if tab_name == "Details":
            details_page = self.driver.find_element(AppiumBy.XPATH, "//android.view.MenuItem[@resource-id='detailsSection']")
            details_page.click()
            print("Successfully switched to details page")
        elif tab_name == "Videos":
            video_page = self.driver.find_element(AppiumBy.XPATH, value="//android.view.MenuItem[@resource-id='videosSection']")
            video_page.click()
            print("Successfully switched to video page")

    def play_video(self):
        time.sleep(4)
        video_play = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Play Video']")
        video_play.click()
        print("Video playing")
        time.sleep(15)

    def pause_video(self):
        self.driver.tap([(500, 900)])
        pause_button = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Pause']")
        pause_button.click()
        print("Pause button clicked")

    def replay_video(self):
        time.sleep(2)
        continue_button = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Continue Watching']")
        continue_button.click()
        print("Continue button clicked")


    def pause_video(self):
    
        self.driver.tap([(500, 900)])  
        time.sleep(2)
        try:
            pause_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Pause']"))
            )
            pause_button.click()
            print("Pause button clicked successfully.")
        except Exception as e:
            print(f"Error while pausing video: {e}")

    def navigate_back(self):
        self.driver.tap([(500, 900)])  
        time.sleep(2)
        try:
            back_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Go Back and continue playing video']"))
            )
            back_button.click()
            print("Navigated back successfully.")
        except Exception as e:
            print(f"Error while navigating back: {e}")

    def logout(self):
        time.sleep(4)
        sign_out = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@resource-id='signOutSideBar']"))
        )
        sign_out.click()
        print("Signed out of the app.")
