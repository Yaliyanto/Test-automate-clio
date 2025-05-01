from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.options.android.uiautomator2.base import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = UiAutomator2Options()
options.udid = '127.0.0.1:62001'  
options.platform_name = 'Android'
options.app_package = 'com.yoripeapp' 
options.app_activity = 'com.yoripeapp.MainActivity' 

# # User can login through google email
def test_login_1():
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    sleep(3)

    driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Google"]').click()
    sleep(3)

    driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.google.android.gms:id/container"])[1]').click()

    try:
        WebDriverWait(driver, 80).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="Terbaru"]')
        ))
        text_terbaru = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Terbaru"]').text
    except:
        text_terbaru = None  # jika elemen tidak ditemukan

    assert text_terbaru == "Terbaru"

# user can not login with invalid email
def test_login_2():

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    sleep(3)

    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Masuk dengan email"]').click()
    sleep(2)
    sub_text = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Masukkan email yang kamu daftarkan di Weyoco."]').text
    sleep(3)
    assert sub_text == "Masukkan email yang kamu daftarkan di Weyoco."
    sleep(3)

    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Masukkan email"]').click()

    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Masukkan email"]').send_keys("ajigusti@yah")

    driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Masuk"]').click()
    sleep(3)


# # user can not login with invalid number phone
def test_login_3():
    sleep(3)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    sleep(3)

    test_masuk_dengan_email = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Masuk dengan email"]').text
    assert test_masuk_dengan_email == "Masuk dengan email"

    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Masukan nomor telepon"]').click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Masukan nomor telepon"]').send_keys("938487383738")
    driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Masuk"]').click()
    sleep(3)
    driver.save_screenshot("screenshot of allert.png")
    driver.quit()

