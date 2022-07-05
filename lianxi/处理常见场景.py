# -- coding: utf-8 --
# @Time : 2022/7/1 9:14
# @Author : siyu.yang
import time,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
# 一、定位一组对象
#    webdriver使用find_element方法定位一个特定的对象，不过我们有时需要定位一组对象，
# webdriver同样提供了定位一组元素的方法叫find_elements。定位一组对象一般用于以下场景：
# .批量操作对象，比如将页面上的checkbox都勾选上
# .先获取一组对象，再再这组对象中过滤需要具体定位的一些对象
driver_path = os.path.join(os.path.dirname(__file__),'../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('C:\\Users\\kcadmin\\Desktop\\ui_base_projec\\element\\element_samples.html')
driver.implicitly_wait(30)
driver.maximize_window()
inputs = driver.find_elements(By.CSS_SELECTOR,'input[type="checkbox"]')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
time.sleep(1)
# 二、层级定位：
#    在实际的项目测试中，经常会遇到无法直接定位到需要选取的元素，但是其弗雷元素比较容易定位，
# 通过定位弗雷元素在遍历其子元素选择需要的目标元素，或者需要定位某个元素下所有的子元素。
#    层级定位的思想式先定位父类呀u盛怒，然后再从对象中精确定位出其它我们需要选取的后代元素怒
# 语法举例：
driver.find_element(By.CSS_SELECTOR,'td.widgetStyle').find_element(By.CSS_SELECTOR,'input.Baidu').click()
time.sleep(1)

# 三、frame中的对象
#    在web应用中经常会出现frame嵌套的应用，假设页面上有A，B两个frame，其中B在A内，那么定位
# B中的内容则需要先到A，再到B。
#    switch_to_frame方法把当前定位的主题切换到frame里，在frame里面实际是签到了另外一个页面
# ,而webdriver每次只能在一个页面识别，所以需要用switch_to_frame方法获取frame中嵌套的页面。
# 举例：
# driver.switch_to.frame('frame1')   #移动到id为frame_1的frame上
# print(driver.find_element(By.CSS_SELECTOR,'div1').text)
driver.switch_to.default_content()  #将是被的主题切除frame
# print(driver.find_element(By.CSS_SELECTOR('id1')).text)
# 备注：switch_to_frame 的参数必须是id或者是name,所以一个frame只要有id和name处理
# 起来是很容易，如果没有的话，两种解决思路：
# 1.让开发加上id或name
# 2.使用xpath 等方式定位然后实现跳针

# 四、浏览器出窗口处理：
#     有时候我们在测试一个web引用的时候会出现多个浏览器窗口的情况，
# webdriver提供了响应的解决方案，如下：
#     首先要获得一个窗口的唯一标识符号（句柄），通过获得的句柄来区分不通的窗口，从而对不通窗口上的元素
# 进行操作：
# 举例：
# driver.get('https://www.jd.com')
# current_handle = driver.current_window_handle
# driver.find_element(By.LINK_TEXT,'秒杀').click()
# driver.find_element(By.LINK_TEXT,'优惠券').click()
# driver.find_element(By.LINK_TEXT,'PLUS会员').click()
# driver.find_element(By.LINK_TEXT,'品牌闪购').click()
# driver.find_element(By.LINK_TEXT,'京东国际').click()
# driver.find_element(By.LINK_TEXT,'京东家电').click()
# driver.find_element(By.LINK_TEXT,'京东超市').click()
# driver.find_element(By.LINK_TEXT,'京东生鲜').click()
# handles = driver.window_handles
# driver.switch_to.window(handles[5])
# driver.find_elements(By.CSS_SELECTOR,'div.quark-5dce12a4324b479a31ebb64a__brand-tab__item-title-imactive')[2].click()
# driver.switch_to.window(current_handle)
# driver.find_element(By.LINK_TEXT,'运动鞋服').click()
# time.sleep(1)
# driver.close()
# 五、alert/confirm/prompt处理
# webdriver中处理原生JS的alert confirm 以及prompt非常方便
#     具体思路是使用switchTo.alert()方法定位到当前的alert/confirm、prompt(这里注意
# 当前页面只能同时含有一个控件，如果多了会报错的，所以这就需要一一处理了)，然后再嗲用Alert方法
# 进行操作，Alert提供了以下几个方法：
# text: 返回alet/confirm/prompt中的文字内容
# accept：点击确认按钮
# dismiss:点击取消按钮，前提是有取消按钮
# sendKys：向prompt中输入文字
# 举例
#alert对话框
driver.find_element(By.NAME,'alterbutton').click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
#prompt对话框
driver.find_element(By.NAME,'promptbutton').click()
driver.switch_to.alert.send_keys('hello promput')
driver.switch_to.alert.dismiss()
time.sleep(1)
driver.find_element(By.NAME,'promptbutton').click()
driver.switch_to.alert.send_keys('hello promput')
driver.switch_to.alert.accept()
driver.switch_to.alert.accept()
#confirm 对话框
driver.find_element(By.NAME,'confirmbutton').click()
driver.switch_to.alert.dismiss()
driver.switch_to.alert.accept()
time.sleep(1)
driver.find_element(By.NAME,'confirmbutton').click()
driver.switch_to.alert.accept()
driver.switch_to.alert.accept()

# 六、下拉框处理：
# web 页面上经常会有下拉框，对下拉框的处理笔架简单，一般分为两种情况：
# 1.下拉框通过元素识别，举例：
driver.find_element(By.XPATH,'//option[@value="mango"]').click()
# 上面的元素下拉框中的选项。

# 2.创建一个select的对象，然后通过响应方法处理，举例：
from selenium.webdriver.support.select import Select
selectElement = driver.find_element(By.XPATH,'//select[@id="Selector"]')
s = Select(selectElement)
s.select_by_index(1)
time.sleep(1)
s.select_by_value('mango')
time.sleep(1)
s.select_by_visible_text('桔子')

# 七、调用javascript:
#     当webdriver遇到无法完成的操作的时候，这个时候可以使用javascript来完成，
# webdriver提供了execute_script() 接口来调用js代码。
# 执行js有两种场景：
# 一种是在页面上直接执行js
# 另一种实在某个已经定位的元素上只想js
# 简单实例：
driver.get('C:\\Users\\kcadmin\\Desktop\\ui_base_projec\\element\\wait.html')
driver.execute_script('alert("hello!")')  #弹出窗口
driver.switch_to.alert.accept()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'button#b').click()
time.sleep(1)
wl = driver.find_element(By.CSS_SELECTOR,'div.red_box')
driver.execute_script("arguments[0].style.border='10px solid purple'",wl)  #给元素加紫色边框
time.sleep(1)
driver.get('https://www.baidu.com')
driver.find_element(By.ID,'kw').send_keys('selenium ui 自动化测试')
js = "var user_input = document.getElementById('su').getAttribute('id');return user_input"
driver.execute_script(js)  #识别并获取对象属性
driver.find_element(By.ID,'su').click()
time.sleep(1)
driver.execute_script("var q=document.documentElement.scrollTop=10000")

# 八、cookies处理:
#    假如我们需要验证浏览器中是否存在cookie,因为基于真实的cookie是无法通过白盒和
# 集成测试完成的，webdriver可以读取、添加和删除cookie信息webdriver操作cookie的方法如下：
# get_cookies()    获取所有cookie信息
# get_cookie(name)   返回特定name有cookie信息
# add_cookie(cookie_dict)   添加cookie，必须有name和value值
# delete_cookie(name)   删除特定部分的cookie信息
# delete_all_cookies()  删除所有cookie信息
# 举例：
#获取所有cookie并打印
driver.get("http://www.youdao.com")
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'],cookie['value']))
    #添加cookie举例
    driver.add_cookie({'name':'key-aaaaa','value':'value-bbbb'})
    driver.delete_cookie("key-aaaaa")  #删除cookie处理常见自动化场景

# 九、验证码处理：
#    对于web应用，很多地方比如登录、发帖都需要输入验证码，类似
# 验证码处理一般有以下几种处理方式：
# 1.去掉验证码。
# 2.万能验证码。
# 3.通过cookie绕过登录。
# 4.图形识别技术识别验证码（存在准确度准确率的问题）

time.sleep(7)
driver.close()
driver.quit()

