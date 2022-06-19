import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome(executable_path='E:\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.jd.com")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"优惠券").click()
driver.find_element(By.LINK_TEXT,"品牌闪购").click()
driver.find_element(By.LINK_TEXT,"拍卖").click()
driver.find_element(By.LINK_TEXT,"京东家电").click()
driver.find_element(By.LINK_TEXT,"京东超市").click()
driver.find_element(By.LINK_TEXT,"京东国际").click()
#句柄
handles = driver.window_handles
for i in handles:
    time.sleep(3)
    driver.switch_to.window(i)
    if driver.current_url == "https://chaoshi.jd.com/":
        break

driver.find_element(By.LINK_TEXT,'超值量贩').click()
time.sleep(4)
driver.quit()

