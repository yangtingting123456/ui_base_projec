# 2022-6-22日作业
# 1、完成ini配置文件和日志文件的使用预习
# 2、完成禅道提交bug的脚本(要有附件)
import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = os.path.join(os.path.abspath(__file__), '../../../driver/chromedriver.exe')
print(driver_path)
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login ')
driver.maximize_window()
driver.implicitly_wait(30)
# 1 登录
driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys("test01")
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("newdream123")
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
# 2 进入测试-bug-提bug模块
driver.find_element(By.LINK_TEXT, '测试').click()
# 3 输入bug信息
driver.find_element(By.CSS_SELECTOR, 'li[data-id="bug"]').click()
driver.find_element(By.LINK_TEXT, '提Bug').click()
# 4 选择项目
driver.find_element(By.CSS_SELECTOR, 'div#product_chosen').click()
driver.find_elements(By.CSS_SELECTOR, 'div.chosen-drop ul.chosen-results li:nth-child(3)')[0].click()
# 5 所属模块
time.sleep(1)
driver.find_elements(By.CSS_SELECTOR, 'div#moduleIdBox div')[0].click()
driver.find_element(By.CSS_SELECTOR, 'ul.chosen-results li:nth-child(7)').click()
# 6 所属项目
driver.find_element(By.CSS_SELECTOR, 'span#projectIdBox').click()
driver.find_elements(By.CSS_SELECTOR, 'div.chosen-drop ul.chosen-results li:nth-child(2)')[2].click()
#7 影响版本
time.sleep(1)
driver.find_elements(By.CSS_SELECTOR, 'li.search-field > input')[0].click()
driver.find_element(By.CSS_SELECTOR, 'li[title="v1.0"]').click()
#8 当前指派
driver.find_element(By.CSS_SELECTOR, 'span.input-group-btn button.btn').click()
driver.find_element(By.CSS_SELECTOR, 'div.input-group a span[title="T:test01"]').click()
time.sleep(1)
element = driver.find_element(By.CSS_SELECTOR, 'li[title="L:兰输"]')
time.sleep(1)
element.click()
#9 选择日期
driver.find_element(By.CSS_SELECTOR, 'input#deadline').send_keys('2022-07-08')
#10 bug 类型
driver.find_element(By.CSS_SELECTOR, 'span[title="代码错误"]').click()
driver.find_element(By.CSS_SELECTOR, 'li[title="界面优化"]').click()
driver.find_elements(By.CSS_SELECTOR, 'div#bugTypeInputGroup div a span')[1].click()
driver.find_element(By.CSS_SELECTOR, 'li[title="Windows"]').click()
driver.find_element(By.CSS_SELECTOR, 'div#bugTypeInputGroup div#browser_chosen').click()
driver.find_element(By.CSS_SELECTOR, 'li[title="chrome"]').click()
#11 bug 标题
driver.find_element(By.NAME, 'title').send_keys('人才中心-新增接口404')
driver.find_elements(By.CSS_SELECTOR, 'span.pri-text')[0].click()
driver.find_elements(By.CSS_SELECTOR, 'span[data-value="2"]')[0].click()
driver.find_elements(By.CSS_SELECTOR, 'span.pri-text')[1].click()
driver.find_elements(By.CSS_SELECTOR, 'span[data-value="1"]')[1].click()
#12 重现步骤
bug_text = driver.find_element(By.CSS_SELECTOR, 'iframe.ke-edit-iframe')
driver.switch_to.frame(bug_text)
driver.find_element(By.CSS_SELECTOR, 'body.article-content').clear()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body.article-content'). \
    send_keys('[步骤]：1.登录成功后。2.点击人才中心。3.点击新增按钮。4.输入内容，点击保存按钮。.\n\n'
              '[结果]：点击保存提示："system error".\n\n'
              '[期望]:点击保存提示："保存成功"')
#13 相关需求
driver.switch_to.default_content()
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'span#storyIdBox').click()
#14 抄送给
driver.find_elements(By.CSS_SELECTOR,'ul.chosen-choices')[1].click()
driver.find_elements(By.CSS_SELECTOR,'li[title="A:admin"]')[1].click()
#15 上传附件
driver.find_element(By.CSS_SELECTOR,'div.file-input-empty button').click()
time.sleep(3)
os.system('E:\\auto3_script\\up.exe')


#16 保存
driver.find_element(By.CSS_SELECTOR,'td button#submit').click()
#17 关闭驱动
time.sleep(10)
driver.quit()
