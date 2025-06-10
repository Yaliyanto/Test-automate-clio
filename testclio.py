from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")
def driver():

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit() 


def test_created_task(driver):
   #open the browser
    driver.get("https://www.clio.com/")
    # click login
    driver.find_element(By.XPATH, "//body/header[@id='page-header']/div[1]/nav[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]").click()
    sleep(2)
    #click sign in to Clio manage
    driver.find_element(By.XPATH, "//a[normalize-space()='Sign in to Clio Manage']").click()
    sleep(2)
    #input email
    driver.find_element(By.ID, "email").send_keys("yaliyanto97@gmail.com")
    sleep(2)
    #click button next
    driver.find_element(By.ID, "next").click()
    sleep(2)
    #input password
    driver.find_element(By.ID, "password").send_keys("kompor123")
    sleep(2)
    # click button sign in
    driver.find_element(By.ID, "signin").click()
    # waiting for element  tittle of Todays's Agenda visible
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='spacing-inline-xs']")))
    #assertion the text title
    text= driver.find_element(By.XPATH, "//h2[@class='spacing-inline-xs']").text
    assert text == "Today's Agenda"
    sleep(2)
    # click button create new
    driver.find_element(By.XPATH, "//span[normalize-space()='Create new']").click()
    # click task
    driver.find_element(By.XPATH, " //a[normalize-space()='Task']").click()
    #input the taskname
    sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Enter task name...']").send_keys("this task name")
    sleep(2)
    #input the description
    driver.find_element(By.XPATH, "//div[@class='fr-element fr-view']").send_keys("this description")
    #save the task
    driver.find_element(By.XPATH, "//span[normalize-space()='Save task']").click()
    sleep(1)
    #assertion the title pop up task created
    text_task_created = driver.find_element(By.XPATH, "//strong[normalize-space()='Task created:']").text 
    sleep(2)
    assert text_task_created == "Task created:"


def test_created_manner(driver):
   #open the browser
    driver.get("https://www.clio.com/")
    # click login
    driver.find_element(By.XPATH, "//body/header[@id='page-header']/div[1]/nav[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]").click()
    sleep(2)
    #click sign in to Clio manage
    driver.find_element(By.XPATH, "//a[normalize-space()='Sign in to Clio Manage']").click()
    sleep(2)
    #input email
    driver.find_element(By.ID, "email").send_keys("yaliyanto97@gmail.com")
    sleep(2)
    #click button next
    driver.find_element(By.ID, "next").click()
    sleep(2)
    #input password
    driver.find_element(By.ID, "password").send_keys("kompor123")
    sleep(2)
    # click button sign in
    driver.find_element(By.ID, "signin").click()
    # waiting for element  tittle of Todays's Agenda visible
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='spacing-inline-xs']")))
    #assertion the text title
    text= driver.find_element(By.XPATH, "//h2[@class='spacing-inline-xs']").text
    sleep(2)
    assert text == "Today's Agenda"
    # click button create new
    driver.find_element(By.XPATH, "//span[normalize-space()='Create new']").click()
    sleep(1)
    #choose matter
    driver.find_element(By.XPATH, "//a[normalize-space()='Matter']").click()
    sleep(1)
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='client_input']")))
    # Click button dropdown client
    sleep(2)
    input_field = driver.find_element(By.XPATH,"//input[@name='client_input']")
    # choose pt abc
    input_field.send_keys(Keys.ARROW_DOWN)
    #input matter description
    driver.find_element(By.XPATH, "//textarea[@placeholder='Enter matter description']").send_keys("Matter descriptionn")
    sleep(2)
    # find element everyone
    driver.find_element(By.XPATH, "//span[@value='advanced']").send_keys(Keys.PAGE_DOWN)
    sleep(2)
    driver.find_element(By.XPATH, "//span[@value='advanced']").send_keys(Keys.PAGE_DOWN)
    sleep(2)
    #choose everyone
    driver.find_element(By.XPATH, "//span[@value='everyone']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//span[normalize-space()='Save matter']").click()
    sleep(5)
    text_dashboard= driver.find_element(By.XPATH, "//span[@class='tab-text'][normalize-space()='Dashboard']").text
    assert text_dashboard == "Dashboard"
    sleep(2)
    driver.save_screenshot("test.png")



    
    



    # //span[@class='k-dropdown-wrap k-state-default k-state-hover k-state-focused k-state-active k-state-border-down']//span[@class='k-icon k-i-arrow-60-down']
    







    

  

  