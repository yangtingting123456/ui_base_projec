from selenium import webdriver
from selenium.webdriver.common.by import By
import os,time

driver_path = os.path.join(os.path.dirname(__file__),'../../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://ctrip.com')
area = driver.find_element(By.CSS_SELECTOR,'input#hotels-destination')
area.clear()
area.send_keys('阿拉尔')
#选择日期
driver.find_element(By.CSS_SELECTOR,'p#checkIn').click()
driver.find_element(By.CSS_SELECTOR,'div.c-calendar__body div').\
    find_element(By.XPATH,'//span[text() = 28]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'div.c-calendar__body div').\
    find_element(By.XPATH,'//span[text() = 30]').click()
time.sleep(1)
#房间人数
driver.find_element(By.CSS_SELECTOR,'div.hs_room-guest-normal_ORFU8').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'div.hs_guest-select_MyRAh > div:nth-child(1) ').\
    find_element(By.CSS_SELECTOR,'div > span;nth-child(3)').click()
time.sleep(1)
driver.quit()

