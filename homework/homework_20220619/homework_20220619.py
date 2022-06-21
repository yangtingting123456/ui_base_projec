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
from selenium import webdriver
from selenium.webdriver.common.by import By
import os,time
driver_path = os.path.join(os.path.abspath(__file__),'../../../driver/chromedriver.exe')
print(driver_path)
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.ctrip.com/')
driver.implicitly_wait(30)
driver.maximize_window()
'''
点击登录按钮，输入用户名和密码，
点击复选框，点击登录按钮
'''
driver.find_element(By.CSS_SELECTOR,'div[class="tl_nfes_home_header_login_title_5neWJ"]').click()
driver.find_element(By.CSS_SELECTOR,'input[class="r_input"]').send_keys('17633710286')
driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys('Qwer@1234')
driver.find_element(By.CSS_SELECTOR,'input[class="agreement-checkbox"]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'input[class="form_btn form_btn--block"]').click()
time.sleep(1)
'''
选择目的地、时间、人数
'''
ruzhu_place=driver.find_element(By.CSS_SELECTOR,'input[class="hs_show-hightlight_CWkCV"]')
ruzhu_place.clear()
time.sleep(1)
ruzhu_place.click()
driver.find_element(By.CSS_SELECTOR,'div[class="hs_hot-city-picker_rBGm- hs_panel-border-shadow_ui12E"] div ul li').click()
# checkIn = driver.find_element(By.CSS_SELECTOR,'p[id="checkIn"]')
# checkIn.click()
# checkIn.clear()
# checkIn.send_keys('7月2日')
# driver.find_element(By.CSS_SELECTOR,'span[class="hs_week_DziA9"]').send_keys('(周六)')
# checkOut = driver.find_element(By.CSS_SELECTOR,'p[id="checkOut"]')
# checkOut.click()
# checkOut.clear()
# checkIn.send_keys('7月3日')
# driver.find_element(By.CSS_SELECTOR,'span[class="hs_week_DziA9"]').send_keys('(周日)')
driver.find_element(By.CSS_SELECTOR,'div[class="hs_search-btn-container_R0HuJ"]').click()
# 搜索


time.sleep(30)
driver.quit()
#    2.2 打开网易云音乐->登录->搜索音乐(城南花已开)->播放三亩地的版本
