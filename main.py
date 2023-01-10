from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime,timedelta
import random
# CREDENTIALS---------------------------------------
email='FS215'
password='S0methingR@ndom'

#Xpaths
loginButton='/html/body/div[1]/div[2]/div[2]/div/form/div/div[3]/button'
menuButton='/html/body/div[1]/div/div[2]/ul[2]/li[4]/a/span'
attendanceButton='/html/body/div[1]/div/div[2]/ul[2]/li[4]/ul/li[2]/div[5]/a/div'

#Variables
driver=None
punchedIn=True

now=datetime.now()
#Entry times
entryMin=now.replace(hour=10,minute=00,second=00)
entryMax=now.replace(hour=11,minute=00,second=00)
exitTime=now.replace(hour=19,minute=30,second=00)

#login
def login():
    global driver
    driver = webdriver.Firefox()
    driver.get("https://fourthsignal.beehivehcm.com/Login")
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH,loginButton).click()
    time.sleep(5)

#PunchIn
def punchIn():
    global driver
    driver.find_element(By.XPATH,menuButton).click()
    driver.find_element(By.XPATH,attendanceButton).click()
    driver.find_element(By.ID,'btnTimeIn')

#PunchOut
def punchOut():
    global driver
    driver.find_element(By.XPATH,menuButton).click()
    driver.find_element(By.XPATH,attendanceButton).click()
    driver.find_element(By.ID,'btnTimeOut')

now=datetime.now()
while True:    
    if not(punchedIn) and now>entryMin and now<entryMax:
        print('logging in------')
        login()
        punchIn()
        driver.close()
        punchedIn=not(punchedIn)
        exitTime=now + timedelta(hours=8,minutes=random.randrange(32,40))
        print(type(exitTime))
    if punchedIn and now>exitTime:
        print('logging out------')
        login()
        punchOut()
        driver.close()
        punchedIn=not(punchedIn)

    now=datetime.now()
    entryMin=now.replace(hour=10,minute=00,second=00)
    entryMax=now.replace(hour=11,minute=00,second=00)
    print('still running------')
    time.sleep(600)
    
