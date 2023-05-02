# Importing required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

# Setting URL and opening driver
URL = "https://tinder.com/"

driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
time.sleep(2)
# Clicking on login button to open the Facebook login popup
login = driver.find_element(By.XPATH,
                            '//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

# Handling Facebook login popup
try:
    time.sleep(2)
    login_with_fb = driver.find_element(By.XPATH, "//div[text()='Log in with Facebook']")
    login_with_fb.click()
    time.sleep(2)
except NoSuchElementException:
    more_opt_but = driver.find_element(By.XPATH, "//div//span//button[text()='More Options']")
    more_opt_but.click()
    time.sleep(2)
    login_with_fb = driver.find_element(By.XPATH, "//div[text()='Log in with Facebook']")
    login_with_fb.click()

# switching control from base window to facebook login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Entering email, password, and logging in
email_input = driver.find_element(By.CSS_SELECTOR, "#email")
email_input.send_keys("YOUR_FACEBOOK_EMAIL_ID")
pass_input = driver.find_element(By.CSS_SELECTOR, "#pass")
pass_input.send_keys("YOUR_FACEBOOK_PASSWORD")
fb_login_button = driver.find_element(By.CSS_SELECTOR, "#loginbutton")
fb_login_button.click()

# switching control back to base window
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(8)

# Handling location, notification, and cookies popups
location_popup = driver.find_element(By.XPATH, "//button//div//div[text() = 'Allow']")
location_popup.click()

time.sleep(2)

notification_popup = driver.find_element(By.XPATH, "//div[text() = 'Not interested']")
notification_popup.click()

time.sleep(2)

cookies_popup = driver.find_element(By.XPATH, "//div[text() = 'I accept']")
cookies_popup.click()
time.sleep(8)

# Loop for liking profiles
for n in range(100):
    time.sleep(2)
    try:

        like_button_tinder = driver.find_element(By.XPATH,
                                                 '//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button_tinder.click()
        print("called")
    except ElementClickInterceptedException:
        try:
            home_shortcut_popup = driver.find_element(By.XPATH, "//div[text() = 'Not interested']")
            home_shortcut_popup.click()
        except NoSuchElementException:
            membership_popup = driver.find_element(By.XPATH, "//button//span[text() = 'Maybe Later']")
            membership_popup.click()
    except NoSuchElementException:
        time.sleep(2)

# Quitting the driver
driver.quit()
