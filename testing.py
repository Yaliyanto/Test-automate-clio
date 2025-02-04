from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()

#login menggunakan email dan password yang valid
def test_positive_login():
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get("https://lapor.folkatech.com/")
    driver.find_element(by.XPATH, "//input[@placeholder='Email']").send_keys("admin@example.com")
    driver.find_element(by.ID, "password").send_keys("password")
    driver.find_element(by.XPATH, "//button[@type='submit']").click()
    #disini saya pasang looping dengan try except agar bisa menunggu element yang diinginkan muncul karena ada perpidahan page
    try:
        element = wait(driver, 8).until(EC.visibility_of_element_located((by.XPATH, "//h3[@class='mb-3']")))
        text = driver.find_element(by.XPATH, "//h3[@class='mb-3']").text
        assert text == "Dashboard"
    finally:
        print("proses selesai.")

#login menggunakan email dan password yang valid kemudian logout
def test_positive_login_logout():
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get("https://lapor.folkatech.com/")
    driver.find_element(by.XPATH, "//input[@placeholder='Email']").send_keys("admin@example.com")
    driver.find_element(by.ID, "password").send_keys("password")
    driver.find_element(by.XPATH, "//button[@type='submit']").click()
    #disini saya pasang looping dengan try except agar bisa menunggu element yang diinginkan muncul karena ada perpidahan page
    try:
        element = wait(driver, 8).until(EC.visibility_of_element_located((by.XPATH, "//h3[@class='mb-3']")))
        text = driver.find_element(by.XPATH, "//h3[@class='mb-3']").text
        assert text == "Dashboard"
    finally:
        print("proses selesai, lanjut ke logout.")
    driver.find_element(by.XPATH,"//img[@alt='Profile Picture']").click()
    driver.find_element(by.XPATH,"//div[normalize-space()='Logout']").click()
    text = driver.find_element(by.XPATH, "//p[@class='mb-0']").text
    assert text == "Masukkan Email dan Password Anda dibawah ini"
    sleep(2)

#login menggunakan email yang valid dan password yang tidak valid
def test_negative_with_email_invalid():
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get("https://lapor.folkatech.com/")
    driver.find_element(by.XPATH, "//input[@placeholder='Email']").send_keys("test123@yahoo.com")
    driver.find_element(by.ID, "password").send_keys("password")
    driver.find_element(by.XPATH, "//button[@type='submit']").click()
    
    try:
        element = wait(driver, 8).until(EC.visibility_of_element_located((by.XPATH, "//label[@role='alert']")))
        text = driver.find_element(by.XPATH, "//label[@role='alert']").text
        assert text == "Login Gagal! Akun tidak ada."
    finally:
        sleep(5)
        driver.quit()

#login menggunakan email yang valid dan password yang tidak valid
def test_negative_with_password_invalid():
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get("https://lapor.folkatech.com/")
    driver.find_element(by.XPATH, "//input[@placeholder='Email']").send_keys("admin@example.com")
    driver.find_element(by.ID, "password").send_keys("passwsaord")
    driver.find_element(by.XPATH, "//button[@type='submit']").click()
    try:
        element = wait(driver, 8).until(EC.visibility_of_element_located((by.XPATH, "//label[@role='alert']")))
        text = driver.find_element(by.XPATH, "//label[@role='alert']").text
        assert text == "Login Gagal! Kata sandi salah."
    finally:
        sleep(5)
        driver.quit()