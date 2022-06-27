# 2022-6-19日作业
# xlwt写、xlrd读
# 1、将禅道的cookie写入到excel表格,然后再读取出来
# import xlrd, xlwt, os
# excel_path = os.path.join(os.path.abspath(__file__), "../data/zentao_login_cookies.xlsx")
# class ExcelUtils:
#     def __init__(self, excel_path=excel_path):
#         self.excel_path = excel_path
#
#     def write_excel(self):
#         wb = xlwt.Workbook()
#         sheet = wb.add_sheet('zentao_cookies')
#         row_list = [["name", "value", "Domain", "path"],
#                     ['zentaosid', 'l97vmm6ovptiq8c47s6unb2e31', '47.107.178.45', '/'],
#                     ['theme', 'default', '47.107.178.45', '/zentao/www/'],
#                     ['device', 'desktop', '47.107.178.45', '/zentao/www/'],
#                     ['lang', 'zh-cn', '47.107.178.45', '/zentao/www/']]
#         for i in range(0, len(row_list)):
#             data = row_list[i]
#             for j in range(0, len(data)):
#                 sheet.write(i, j,data[j])
#         wb.save(self.excel_path)
#
#     def read_excel(self):
#         wk = xlrd.open_workbook(self.excel_path)
#         sheet = wk.sheet_by_name("zentao_cookies")
#         rows = sheet.nrows
#         cols = sheet.ncols
#         cookies_list = []
#         for i in range(cols + 1):
#             cookie_list = []
#             for j in range(rows - 1):
#                 cookie_list.append(sheet.cell_value(i, j))
#             cookies_list.append(cookie_list)
#         return cookies_list
#
#     def list_to_change_dic(self):
#         c= []
#         for i in range(0, 4):
#             b = []
#             for j in range (1,5):
#              a = {self.read_excel()[0][j-1]: self.read_excel()[i+1][j-1]}
#              b.append(a)
#             c.append(b)
#         return c
#
# if __name__ == '__main__':
#     ecl_util = ExcelUtils()
#     ecl_util.write_excel()
#     # ecl_util.read_excel()
#     # for i in range(0,4):
#     # print(ecl_util.list_to_change_dic())
#

# 2、完成自动化流程
#    2.1 登录携程->选择目的地、时间、人数->搜索->点击查看详情->预定(不付款)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import os,time
# driver_path = os.path.join(os.path.abspath(__file__),'../../../driver/chromedriver.exe')
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.ctrip.com/')
# driver.implicitly_wait(30)
# driver.maximize_window()
# '''
# 点击登录按钮，输入用户名和密码，
# 点击复选框，点击登录按钮
# '''
# driver.find_element(By.CSS_SELECTOR,'div[class="tl_nfes_home_header_login_title_5neWJ"]').click()
# driver.find_element(By.CSS_SELECTOR,'input[class="r_input"]').send_keys('17633710286')
# driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys('Qwer@1234')
# driver.find_element(By.CSS_SELECTOR,'input[class="agreement-checkbox"]').click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,'input[class="form_btn form_btn--block"]').click()
# time.sleep(1)
# '''
# 选择入住酒店目的地、时间、人数
# '''
# hotels_destination = driver.find_element(By.ID,'hotels-destination')
# hotels_destination.clear()
# hotels_destination.send_keys('西安')
# #选择入住日期
# driver.find_element(By.ID,'checkIn').click()
# driver.find_elements(By.CSS_SELECTOR,'div.c-calendar__body  div.c-calendar-month div.c-calendar-month__days ul:nth-child(2)')[0].click()
# driver.find_elements(By.CSS_SELECTOR,'div.c-calendar__body  div.c-calendar-month div.c-calendar-month__days ul:nth-child(5)')[1].click()
# #选择房间以及住客
# driver.find_element(By.CSS_SELECTOR,'div[class="hs_room-guest-normal_ORFU8"]').click()
# driver.find_elements(By.CSS_SELECTOR,'div.hs_guest-select_MyRAh div.hs_actions_o7WkH span:nth-child(3)')[0].click()
# driver.find_element(By.CSS_SELECTOR,'span.hs_done-span_-EIBx').click()
# #选择星级
# driver.find_element(By.CSS_SELECTOR,'div.hs_star-rate-normal_4Xd1x').click()
# driver.find_elements(By.CSS_SELECTOR,'div.hs_child-kid_o2dPC')[2].click()
# driver.find_element(By.CSS_SELECTOR,'span.hs_done-span_bF5dT').click()
# #点击搜索
# driver.find_element(By.CSS_SELECTOR,'div.hs_search-btn-container_R0HuJ').click()
# time.sleep(10)
# driver.quit()
#    2.2 打开网易云音乐->登录->搜索音乐(城南花已开)->播放三亩地的版本
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os,time
driver_path = os.path.join(os.path.abspath(__file__),'../../../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://music.163.com/')
driver.refresh()
driver.implicitly_wait(30)
driver.maximize_window()
#登录
time.sleep(1)
driver.find_element(By.LINK_TEXT,'登录').click()
driver.find_element(By.CSS_SELECTOR,'div._2t0Z3pyt').find_element(By.LINK_TEXT,'选择其他登录模式').click()
driver.find_element(By.ID,'j-official-terms').click()
driver.find_element(By.LINK_TEXT,'QQ登录').click()
#QQ扫码登录
time.sleep(30)
#搜索音乐(城南花已开)
driver.find_element(By.ID,'srch').send_keys('城南花已开')
time.sleep(2)
driver.find_element(By.ID,'srch').send_keys(Keys.ENTER)
time.sleep(2)
driver.switch_to.frame('g_iframe')
# driver.find_elements(By.CSS_SELECTOR,'div.srchsongst > div >div:nth-child(1)')[0].click()
driver.find_element(By.CSS_SELECTOR,'a#song_468176711').click()



time.sleep(60)
driver.quit()
